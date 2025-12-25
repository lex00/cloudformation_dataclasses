"""
Resource loader with topological import ordering.

This module provides a helper for loading resource modules in dependency order,
solving circular import issues when resources reference each other.

The loader:
1. Parses source files to find class definitions and ref() calls
2. Builds a dependency graph
3. Imports modules in topological order
4. Injects earlier resources into later modules' namespace

Usage in resources/__init__.py:
    from cloudformation_dataclasses.core.resource_loader import setup_resources
    setup_resources(__file__, __name__, globals())
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

from cloudformation_dataclasses.stubs import (
    find_class_definitions as _find_class_definitions,
    generate_stub_file as _generate_stub_file,
)


def _find_class_refs_in_source(source: str) -> set[str]:
    """Extract class names from ref(X), get_att(X, ...), and Ref[X] patterns.

    Matches identifiers (not quoted strings like ref("X")).
    Handles both PascalCase (MyResource) and camelCase (myResource) class names.
    """
    refs: set[str] = set()
    # Match ref(ClassName) - any valid identifier, not quoted
    for match in re.finditer(r'\bref\(([A-Za-z_][A-Za-z0-9_]*)\)', source):
        refs.add(match.group(1))
    # Match get_att(ClassName, ...) - any valid identifier, not quoted
    for match in re.finditer(r'\bget_att\(([A-Za-z_][A-Za-z0-9_]*)\s*,', source):
        refs.add(match.group(1))
    # Match Ref[ClassName] type annotations
    for match in re.finditer(r'\bRef\[([A-Za-z_][A-Za-z0-9_]*)\]', source):
        refs.add(match.group(1))
    # Match GetAtt[ClassName] type annotations (if used)
    for match in re.finditer(r'\bGetAtt\[([A-Za-z_][A-Za-z0-9_]*)\]', source):
        refs.add(match.group(1))
    return refs


def _topological_sort(deps: dict[str, set[str]]) -> list[str]:
    """Kahn's algorithm for topological sort with cycle handling.

    Args:
        deps: Dict mapping module name to set of module names it depends on.

    Returns:
        List of module names in dependency order (dependencies first).
        Handles cycles by breaking them and continuing the sort.
    """
    # Make a mutable copy of deps
    remaining_deps: dict[str, set[str]] = {m: set(d) for m, d in deps.items()}

    result: list[str] = []

    while remaining_deps:
        # Find modules with no remaining dependencies
        ready = [m for m, d in remaining_deps.items() if len(d) == 0]

        if ready:
            # Process modules with no dependencies
            for m in sorted(ready):  # Sort for determinism
                result.append(m)
                del remaining_deps[m]
                # Remove this module from others' dependency sets
                for other_deps in remaining_deps.values():
                    other_deps.discard(m)
        else:
            # All remaining modules have dependencies -> there's a cycle
            # Find the actual cycle members (modules that depend on each other)
            # A cycle member is one whose dependencies are also in remaining_deps
            # AND one of those deps depends back on it (directly or indirectly)

            # Simple heuristic: pick the module that is depended upon by most
            # other remaining modules - this breaks the cycle at a "hub" node
            # which allows more modules to proceed
            dep_count: dict[str, int] = {m: 0 for m in remaining_deps}
            for d in remaining_deps.values():
                for dep in d:
                    if dep in dep_count:
                        dep_count[dep] += 1

            # Pick the most-depended-upon module, with alphabetical tiebreaker
            cycle_breaker = max(
                remaining_deps.keys(),
                key=lambda m: (dep_count[m], -ord(m[0]) if m else 0, m)
            )
            result.append(cycle_breaker)
            del remaining_deps[cycle_breaker]
            # Remove this module from others' dependency sets
            for other_deps in remaining_deps.values():
                other_deps.discard(cycle_breaker)

    return result


def setup_resources(
    init_file: str, package_name: str, package_globals: dict[str, Any]
) -> None:
    """Set up resource imports with topological ordering.

    This function:
    1. Parses all .py files in the resources directory
    2. Builds a dependency graph from ref()/get_att() calls
    3. Imports modules in topological order
    4. Injects previously-loaded classes into each module's namespace

    Args:
        init_file: Path to __init__.py (__file__)
        package_name: Package name (__name__)
        package_globals: Package globals dict (globals())
    """
    pkg_path = Path(init_file).parent

    # 1. Read all module sources and find classes/refs
    module_sources: dict[str, str] = {}
    module_classes: dict[str, list[str]] = {}

    for file in pkg_path.glob("*.py"):
        if file.name.startswith("_"):
            continue
        source = file.read_text()
        module_name = file.stem
        module_sources[module_name] = source
        module_classes[module_name] = _find_class_definitions(source)

    # 2. Build class -> module map
    class_to_module: dict[str, str] = {}
    for mod, classes in module_classes.items():
        for cls in classes:
            class_to_module[cls] = mod

    # 3. Build dependency graph (module -> set of modules it depends on)
    deps: dict[str, set[str]] = {mod: set() for mod in module_sources}
    for mod, source in module_sources.items():
        for ref_class in _find_class_refs_in_source(source):
            if ref_class in class_to_module:
                dep_mod = class_to_module[ref_class]
                if dep_mod != mod:
                    deps[mod].add(dep_mod)

    # 4. Topological sort
    import_order = _topological_sort(deps)

    # 5. Import in order, injecting shared namespace BEFORE each module executes
    # Start with params from package globals (imported via `from .params import *`)
    # Filter to only include names ending in "Param" to avoid injecting modules/functions
    # Also set _logical_id on Parameter instances (strip "Param" suffix for CloudFormation name)
    shared_namespace: dict[str, Any] = {}
    for name, obj in package_globals.items():
        if name.endswith("Param"):
            # Set the logical ID on the Parameter instance (strip "Param" suffix)
            if hasattr(obj, "_logical_id"):
                obj._logical_id = name[:-5]  # Remove "Param" suffix
            shared_namespace[name] = obj
    all_names: list[str] = []

    for mod_name in import_order:
        full_mod_name = f"{package_name}.{mod_name}"

        # Skip if already imported (shouldn't happen with topological order)
        if full_mod_name in sys.modules:
            module = sys.modules[full_mod_name]
        else:
            # Load module with namespace injection BEFORE execution
            module = _load_module_with_namespace(
                mod_name, full_mod_name, pkg_path, shared_namespace
            )

        # Extract classes from this module and add to shared namespace
        for cls_name in module_classes.get(mod_name, []):
            if hasattr(module, cls_name):
                obj = getattr(module, cls_name)
                shared_namespace[cls_name] = obj
                package_globals[cls_name] = obj
                all_names.append(cls_name)

    # Set __all__ for star imports
    package_globals["__all__"] = all_names

    # Generate __init__.pyi for IDE type checking support
    _generate_stub_file(pkg_path, all_names, module_classes)


def _load_module_with_namespace(
    mod_name: str,
    full_mod_name: str,
    pkg_path: Path,
    namespace: dict[str, Any],
) -> ModuleType:
    """Load a module, injecting namespace before execution.

    This allows ref(ClassName) to resolve during class body evaluation.
    """
    file_path = pkg_path / f"{mod_name}.py"

    # Create module spec
    spec = importlib.util.spec_from_file_location(full_mod_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {full_mod_name} from {file_path}")

    # Create module object
    module = importlib.util.module_from_spec(spec)

    # Inject shared namespace BEFORE execution
    # This makes sibling resource classes available during class body evaluation
    for name, obj in namespace.items():
        setattr(module, name, obj)

    # Register in sys.modules before execution (standard Python behavior)
    sys.modules[full_mod_name] = module

    # Execute the module code
    spec.loader.exec_module(module)

    return module
