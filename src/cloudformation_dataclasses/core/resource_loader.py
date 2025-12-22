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
from collections import deque
from pathlib import Path
from types import ModuleType
from typing import Any


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


def _find_class_definitions(source: str) -> list[str]:
    """Extract class names defined in a source file."""
    return re.findall(r'^class (\w+)', source, re.MULTILINE)


def _topological_sort(deps: dict[str, set[str]]) -> list[str]:
    """Kahn's algorithm for topological sort.

    Args:
        deps: Dict mapping module name to set of module names it depends on.

    Returns:
        List of module names in dependency order (dependencies first).
    """
    # in_degree[m] = number of dependencies m has that haven't been processed yet
    in_degree: dict[str, int] = {m: len(d) for m, d in deps.items()}

    # Start with modules that have no dependencies
    queue: deque[str] = deque(m for m, deg in in_degree.items() if deg == 0)
    result: list[str] = []

    while queue:
        m = queue.popleft()
        result.append(m)
        # For each module that depends on m, decrement its in-degree
        for other, other_deps in deps.items():
            if m in other_deps:
                in_degree[other] -= 1
                if in_degree[other] == 0:
                    queue.append(other)

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
    shared_namespace: dict[str, Any] = {}
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
