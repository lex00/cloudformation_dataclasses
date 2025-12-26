"""
Stub file generator for IDE type checking.

This module generates .pyi stub files so that IDEs like VSCode/Pylance
can understand the dynamic imports used in cloudformation_dataclasses resource packages.

The problem: Resource files use dynamic imports which work at runtime because
setup_resources() dynamically loads and injects names. But static analyzers
can't see these dynamic exports.

The solution: Generate .pyi stub files that explicitly declare what's exported.

Supports two package structures:
1. New flat structure: package/__init__.py with setup_resources(__file__)
   - Generates package/__init__.pyi with all re-exports
2. Old stack/ structure: package/stack/__init__.py with setup_resources
   - Generates stack/__init__.pyi for backwards compatibility

Usage:
    # Generate stubs for a directory
    from cloudformation_dataclasses.stubs import generate_stubs_for_path
    generate_stubs_for_path(Path("."))

    # Or use the CLI
    cfn-dataclasses stubs
    cfn-dataclasses stubs --watch
"""

from __future__ import annotations

import re
from pathlib import Path

from cloudformation_dataclasses.constants import CLASS_NAME_PATTERN

# List of names exported by cloudformation_dataclasses.core
# Duplicated here to avoid circular import (core.resource_loader imports from stubs)
CORE_ALL = [
    # Constants
    "ARN",
    "ARN_EQUALS",
    "ARN_LIKE",
    "BOOL",
    "IP_ADDRESS",
    "NUMBER",
    "STRING",
    "STRING_EQUALS",
    "STRING_LIKE",
    "STRING_NOT_EQUALS",
    "STRING_NOT_LIKE",
    # Enums
    "ConditionOperator",
    "IpProtocol",
    "ParameterType",
    # Core classes
    "CloudFormationResource",
    "Condition",
    "DenyStatement",
    "Mapping",
    "Output",
    "Parameter",
    "PolicyDocument",
    "PolicyStatement",
    "ResourceRegistry",
    "Tag",
    "Template",
    # Decorators and helpers
    "cloudformation_dataclass",
    "get_att",
    "ref",
    "registry",
    "setup_resources",
    # Type wrappers
    "GetAtt",
    "Ref",
    # Intrinsic functions
    "Base64",
    "Cidr",
    "FindInMap",
    "GetAZs",
    "If",
    "ImportValue",
    "Join",
    "Select",
    "Split",
    "Sub",
    "Transform",
    # Pseudo-parameters
    "AWS_ACCOUNT_ID",
    "AWS_NO_VALUE",
    "AWS_NOTIFICATION_ARNS",
    "AWS_PARTITION",
    "AWS_REGION",
    "AWS_STACK_ID",
    "AWS_STACK_NAME",
    "AWS_URL_SUFFIX",
]


def expand_star_import(import_line: str) -> tuple[str, list[str]]:
    """Expand a star import to explicit imports if from a known module.

    For known modules (like cloudformation_dataclasses.core), expands
    `from x import *` to explicit imports so Pylance can resolve them.

    Args:
        import_line: An import statement line

    Returns:
        Tuple of (expanded_import_line, list_of_names).
        If not a star import or unknown module, returns original line
        with empty list.
    """
    # Strip noqa comments
    clean_line = import_line
    if "#" in clean_line:
        clean_line = clean_line.split("#")[0].strip()

    if "from cloudformation_dataclasses.core import *" in clean_line:
        # Expand to explicit imports
        names = sorted(CORE_ALL)
        expanded = f"from cloudformation_dataclasses.core import {', '.join(names)}"
        return expanded, names

    # Not a star import we can expand
    return import_line, []


def find_class_definitions(source: str) -> list[str]:
    """Extract class names defined in a source file."""
    return CLASS_NAME_PATTERN.findall(source)


def find_param_definitions(source: str) -> list[str]:
    """Extract parameter names (XxxParam = Parameter(...)) from a source file."""
    params: list[str] = []
    for match in re.finditer(
        r"^([A-Z][A-Za-z0-9]*Param)\s*=\s*Parameter\(", source, re.MULTILINE
    ):
        params.append(match.group(1))
    return params


def extract_import_names(import_stmt: str) -> list[str]:
    """Extract imported names from an import statement.

    Handles:
    - from x import a, b, c
    - from x import (a, b, c)
    - from x import a as alias
    - from x import *  (returns empty list - star imports handled separately)
    - import x, y, z
    - Comments like # noqa: F403 are stripped
    """
    names: list[str] = []

    # Remove newlines and extra whitespace
    import_stmt = " ".join(import_stmt.split())

    # Strip trailing comments (e.g., # noqa: F403)
    if "#" in import_stmt:
        import_stmt = import_stmt.split("#")[0].strip()

    if import_stmt.startswith("from "):
        # from x import a, b, c  OR  from x import (a, b, c)
        if " import " in import_stmt:
            imports_part = import_stmt.split(" import ", 1)[1]
            # Remove parentheses
            imports_part = imports_part.replace("(", "").replace(")", "")

            # Handle star imports - return empty (caller handles these specially)
            if imports_part.strip() == "*":
                return []

            # Split by comma
            for item in imports_part.split(","):
                item = item.strip()
                if " as " in item:
                    # from x import a as b -> use 'b'
                    names.append(item.split(" as ")[1].strip())
                elif item and item != "*":
                    names.append(item)
    elif import_stmt.startswith("import "):
        # import x, y, z
        imports_part = import_stmt[7:]  # Remove "import "
        for item in imports_part.split(","):
            item = item.strip()
            if " as " in item:
                names.append(item.split(" as ")[1].strip())
            elif item:
                # For 'import x.y.z', the available name is 'x'
                names.append(item.split(".")[0])

    return names


def generate_stub_file(
    package_path: Path,
    all_names: list[str] | None = None,
    module_classes: dict[str, list[str]] | None = None,
) -> bool:
    """Generate .pyi stub files for IDE type checking.

    This allows IDEs like VSCode/Pylance to understand what names are
    exported from resource packages, even though they're loaded dynamically.

    Supports two package structures:
    1. New flat structure: package/__init__.py with setup_resources()
       - Generates package/__init__.pyi with all re-exports
    2. Old stack/ structure: package/stack/__init__.py
       - Generates stack/__init__.pyi and package/__init__.pyi

    Args:
        package_path: Path to the package directory (either package/ or package/stack/)
        all_names: Optional list of all exported names (computed if not provided)
        module_classes: Optional dict of module -> class names (computed if not provided)

    Returns:
        True if stubs were generated/updated, False if unchanged
    """
    # If not provided, scan the package directory for resource modules
    if module_classes is None:
        module_classes = {}
        for file in package_path.glob("*.py"):
            if file.name.startswith("_"):
                continue
            source = file.read_text()
            module_name = file.stem
            module_classes[module_name] = find_class_definitions(source)

    if all_names is None:
        all_names = []
        for classes in module_classes.values():
            all_names.extend(classes)

    changed = False

    # Generate package/__init__.pyi
    init_stub_path = package_path / "__init__.pyi"
    init_lines = ['"""Auto-generated stub for IDE type checking."""', ""]

    # Read the __init__.py to extract imports
    init_file = package_path / "__init__.py"
    imported_names: list[str] = []
    param_names: list[str] = []

    if init_file.exists():
        init_source = init_file.read_text()
        in_import = False
        import_buffer: list[str] = []

        for line in init_source.splitlines():
            if in_import:
                import_buffer.append(line)
                if ")" in line:
                    # End of multi-line import
                    full_import = "\n".join(import_buffer)
                    init_lines.append(full_import)
                    imported_names.extend(extract_import_names(full_import))
                    import_buffer = []
                    in_import = False
            elif line.startswith("from ") or line.startswith("import "):
                if "(" in line and ")" not in line:
                    # Start of multi-line import
                    in_import = True
                    import_buffer = [line]
                else:
                    # Skip star imports from .params and .outputs - we'll add explicit imports later
                    if "from .params import *" in line or "from .outputs import *" in line:
                        continue
                    # Try to expand star imports from known modules
                    expanded_line, star_names = expand_star_import(line)
                    init_lines.append(expanded_line)
                    if star_names:
                        imported_names.extend(star_names)
                    else:
                        imported_names.extend(extract_import_names(line))

    init_lines.append("")

    # Re-export params from params.py
    params_file = package_path / "params.py"
    if params_file.exists():
        param_names = find_param_definitions(params_file.read_text())
        for param in sorted(param_names):
            init_lines.append(f"from .params import {param} as {param}")

    # Re-export all classes from resource modules
    all_resource_classes: list[str] = []
    for mod_name, classes in sorted(module_classes.items()):
        if classes:
            for cls in sorted(classes):
                init_lines.append(f"from .{mod_name} import {cls} as {cls}")
                all_resource_classes.append(cls)

    init_lines.append("")

    # Build __all__ for star imports - Pylance needs this to resolve imports
    all_exports = imported_names + param_names + all_resource_classes

    init_lines.append(f"__all__: list[str] = {sorted(set(all_exports))!r}")
    init_lines.append("")

    if _write_stub_if_changed(init_stub_path, "\n".join(init_lines)):
        changed = True

    return changed


def _write_stub_if_changed(stub_path: Path, content: str) -> bool:
    """Write stub file only if content has changed.

    Returns True if file was written, False if unchanged.
    """
    try:
        existing = stub_path.read_text()
        if existing == content:
            return False
    except FileNotFoundError:
        pass

    stub_path.write_text(content)
    return True


def is_resource_package(path: Path) -> bool:
    """Check if a directory is a cloudformation_dataclasses resource package.

    A resource package has __init__.py that calls setup_resources(__file__).

    Supports two structures:
    1. New flat structure: package/__init__.py with setup_resources(__file__)
    2. Old stack/ structure: package/stack/__init__.py with setup_resources
    """
    init_file = path / "__init__.py"
    if not init_file.exists():
        return False

    content = init_file.read_text()
    # Check for setup_resources(__file__ pattern (new flat structure)
    # or just setup_resources (old stack/ structure for backwards compat)
    return "setup_resources(__file__" in content or "setup_resources" in content


def find_resource_packages(root: Path) -> list[Path]:
    """Find all resource packages under a root directory.

    Looks for directories with __init__.py that contain setup_resources(__file__).

    Supports two structures:
    1. New flat structure: any directory with setup_resources(__file__) in __init__.py
    2. Old stack/ structure: directories named 'stack' with setup_resources
    """
    packages: list[Path] = []

    # Find all directories with __init__.py
    for init_file in root.rglob("__init__.py"):
        package_dir = init_file.parent
        if is_resource_package(package_dir):
            packages.append(package_dir)

    return packages


def generate_stubs_for_path(path: Path) -> int:
    """Generate stubs for all resource packages under a path.

    Args:
        path: Directory to scan for resource packages

    Returns:
        Number of resource packages processed
    """
    path = path.resolve()

    # Check if path itself is a resource package
    if is_resource_package(path):
        packages = [path]
    else:
        packages = find_resource_packages(path)

    for package_path in packages:
        generate_stub_file(package_path)

    return len(packages)


# Backwards compatibility aliases
is_stack_package = is_resource_package
find_stack_packages = find_resource_packages
