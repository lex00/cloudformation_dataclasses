"""Runtime registry for AWS resource and PropertyType class discovery.

This module scans the aws/ package to build mappings from CloudFormation types
to Python classes. The registries are lazily built on first access.
"""

import re
from pathlib import Path
from typing import Any, Callable, Optional

# =============================================================================
# Shared Regex Patterns
# =============================================================================

# Pattern to extract class name from class definition (captures name only)
CLASS_NAME_PATTERN = re.compile(r"^class\s+(\w+)", re.MULTILINE)

# Pattern to extract class name and parent from class definition
CLASS_WITH_PARENT_PATTERN = re.compile(r"^class\s+(\w+)\s*\(\s*(\w+)\s*\)")


# =============================================================================
# AWS Module Scanner (shared infrastructure)
# =============================================================================


def _get_aws_dir() -> Optional[Path]:
    """Get the path to the AWS modules directory."""
    try:
        import cloudformation_dataclasses.aws as aws_pkg

        return Path(aws_pkg.__file__).parent
    except (ImportError, AttributeError):
        return None


def _scan_aws_modules(
    on_init_file: Optional[Callable[[Path, str, str], None]] = None,
    on_submodule: Optional[Callable[[Path, str, str], None]] = None,
    on_flat_file: Optional[Callable[[Path, str, str], None]] = None,
) -> None:
    """
    Unified scanner for AWS modules directory.

    Iterates through the aws/ directory and calls callbacks for each file type:
    - on_init_file(path, module_name, content): Package __init__.py (e.g., ec2/__init__.py)
    - on_submodule(path, module_name, content): Package submodules (e.g., ec2/instance.py)
    - on_flat_file(path, module_name, content): Flat module files (legacy, e.g., s3.py)

    All callbacks receive: (file_path: Path, module_name: str, content: str)
    For submodules, module_name is dotted (e.g., "ec2.instance").
    """
    aws_dir = _get_aws_dir()
    if not aws_dir:
        return

    for entry in aws_dir.iterdir():
        if entry.name.startswith("_"):
            continue

        if entry.is_file() and entry.suffix == ".py":
            # Flat module: aws/s3.py (legacy)
            if on_flat_file:
                try:
                    content = entry.read_text()
                    on_flat_file(entry, entry.stem, content)
                except Exception:
                    pass

        elif entry.is_dir():
            # Nested package: aws/ec2/
            service_name = entry.name

            # Process __init__.py (Resources)
            init_file = entry / "__init__.py"
            if init_file.exists() and on_init_file:
                try:
                    content = init_file.read_text()
                    on_init_file(init_file, service_name, content)
                except Exception:
                    pass

            # Process submodules (PropertyTypes)
            if on_submodule:
                for py_file in entry.glob("*.py"):
                    if py_file.name.startswith("_"):
                        continue
                    if py_file.name == "__init__.py":
                        continue
                    try:
                        content = py_file.read_text()
                        full_module = f"{service_name}.{py_file.stem}"
                        on_submodule(py_file, full_module, content)
                    except Exception:
                        pass


# =============================================================================
# Resource Type Registry
# =============================================================================

# Cache for resource type mappings
_RESOURCE_TYPE_MAP: dict[str, tuple[str, str]] = {}
_RESOURCE_TYPE_MAP_BUILT = False


def _build_resource_type_map() -> None:
    """Build mapping from CloudFormation types to Python classes by scanning aws modules.

    Resources are in __init__.py files for nested packages.
    Thread-safe: uses local dict and atomic assignment.
    """
    global _RESOURCE_TYPE_MAP, _RESOURCE_TYPE_MAP_BUILT
    if _RESOURCE_TYPE_MAP_BUILT:
        return

    # Build into a local dict first, then assign atomically
    local_map: dict[str, tuple[str, str]] = {}

    # Pattern to find resource_type class variable assignments
    resource_type_pattern = re.compile(
        r'resource_type:\s*ClassVar\[str\]\s*=\s*["\']([^"\']+)["\']'
    )

    def scan_for_resources(path: Path, module_name: str, content: str) -> None:
        """Extract resource type mappings from file content."""
        current_class = None
        for line in content.split("\n"):
            class_match = CLASS_NAME_PATTERN.match(line)
            if class_match:
                current_class = class_match.group(1)
                continue

            if current_class:
                type_match = resource_type_pattern.search(line)
                if type_match:
                    resource_type = type_match.group(1)
                    local_map[resource_type] = (module_name, current_class)

    # Resources are only in __init__.py (nested) or flat .py files (legacy)
    _scan_aws_modules(
        on_init_file=scan_for_resources,
        on_flat_file=scan_for_resources,
    )

    # Atomic assignment after building is complete
    _RESOURCE_TYPE_MAP.update(local_map)
    _RESOURCE_TYPE_MAP_BUILT = True


def resolve_resource_type(resource_type: str) -> Optional[tuple[str, str]]:
    """
    Resolve a CloudFormation resource type to Python module and class.

    Args:
        resource_type: CloudFormation resource type (e.g., "AWS::S3::Bucket")

    Returns:
        Tuple of (module_name, class_name) or None if unknown.
        module_name is relative to cloudformation_dataclasses.aws
    """
    _build_resource_type_map()
    return _RESOURCE_TYPE_MAP.get(resource_type)


def get_all_resource_types() -> dict[str, tuple[str, str]]:
    """Get all known resource types and their Python mappings."""
    _build_resource_type_map()
    return _RESOURCE_TYPE_MAP.copy()


# =============================================================================
# PropertyType Registry
# =============================================================================

# Stores information about PropertyType classes for code generation
# Structure: {
#   (module_name, class_name): {
#       "cf_to_python": {"CFPropertyName": "python_field_name"},
#       "python_to_cf": {"python_field_name": "CFPropertyName"},
#       "field_types": {"python_field_name": "type_annotation_string"},
#   }
# }
_PROPERTY_TYPE_MAP: dict[tuple[str, str], dict[str, Any]] = {}
_PROPERTY_TYPE_MAP_BUILT = False

# Reverse lookup: CloudFormation property name -> list of (module, class) that use it
# Used for quick lookups when we see a CF property name in a dict
_CF_PROPERTY_TO_CLASSES: dict[str, list[tuple[str, str]]] = {}


def _build_property_type_map() -> None:
    """Build mapping of PropertyType classes and their field information.

    PropertyTypes are in submodules (ec2/instance.py) for nested packages,
    and the module_name will be "ec2.instance" to enable correct imports.
    Thread-safe: uses local dicts and atomic assignment.
    """
    global _PROPERTY_TYPE_MAP, _PROPERTY_TYPE_MAP_BUILT, _CF_PROPERTY_TO_CLASSES
    if _PROPERTY_TYPE_MAP_BUILT:
        return

    # Build into local dicts first
    local_type_map: dict[tuple[str, str], dict[str, Any]] = {}
    local_cf_to_classes: dict[str, list[tuple[str, str]]] = {}

    # Patterns for parsing
    field_pattern = re.compile(r"^\s+(\w+):\s*(.+?)\s*(?:=|$)")
    mapping_entry_pattern = re.compile(r'"(\w+)":\s*"(\w+)"')

    def _register_property_type(
        module_name: str, class_name: str, mappings: dict[str, str], fields: dict[str, str]
    ) -> None:
        """Register a PropertyType class in the local maps."""
        key = (module_name, class_name)
        cf_to_python = {v: k for k, v in mappings.items()}
        local_type_map[key] = {
            "cf_to_python": cf_to_python,
            "python_to_cf": mappings.copy(),
            "field_types": fields.copy(),
        }
        for cf_name in cf_to_python:
            if cf_name not in local_cf_to_classes:
                local_cf_to_classes[cf_name] = []
            local_cf_to_classes[cf_name].append(key)

    def scan_for_property_types(path: Path, module_name: str, content: str) -> None:
        """Scan content for PropertyType classes and register them."""
        current_class: Optional[str] = None
        current_parent: Optional[str] = None
        current_mappings: dict[str, str] = {}
        current_fields: dict[str, str] = {}
        in_class = False

        lines = content.split("\n")
        for i, line in enumerate(lines):
            # Check for class definition
            class_match = CLASS_WITH_PARENT_PATTERN.match(line)
            if class_match:
                # Save previous class if it was a PropertyType
                if current_class and current_parent == "PropertyType" and current_mappings:
                    _register_property_type(
                        module_name, current_class, current_mappings, current_fields
                    )

                current_class = class_match.group(1)
                current_parent = class_match.group(2)
                current_mappings = {}
                current_fields = {}
                in_class = True
                continue

            if not in_class or not current_class:
                continue

            # Check for _property_mappings
            if "_property_mappings" in line:
                # Try to find the full mapping (may span multiple lines)
                mapping_text = line
                j = i
                while "}" not in mapping_text and j < len(lines) - 1:
                    j += 1
                    mapping_text += lines[j]
                # Extract all mappings
                for match in mapping_entry_pattern.finditer(mapping_text):
                    python_name, cf_name = match.groups()
                    current_mappings[python_name] = cf_name
                continue

            # Check for field type annotations
            field_match = field_pattern.match(line)
            if field_match:
                field_name, type_annotation = field_match.groups()
                if not field_name.startswith("_"):
                    current_fields[field_name] = type_annotation

        # Don't forget the last class
        if current_class and current_parent == "PropertyType" and current_mappings:
            _register_property_type(module_name, current_class, current_mappings, current_fields)

    # PropertyTypes can be in __init__.py (legacy), submodules, or flat files
    _scan_aws_modules(
        on_init_file=scan_for_property_types,
        on_submodule=scan_for_property_types,
        on_flat_file=scan_for_property_types,
    )

    # Atomic assignment after building is complete
    _PROPERTY_TYPE_MAP.update(local_type_map)
    _CF_PROPERTY_TO_CLASSES.update(local_cf_to_classes)
    _PROPERTY_TYPE_MAP_BUILT = True


def get_property_type_info(module: str, class_name: str) -> Optional[dict[str, Any]]:
    """
    Get information about a PropertyType class.

    Args:
        module: Module name (e.g., "s3")
        class_name: Class name (e.g., "BucketEncryption")

    Returns:
        Dict with cf_to_python, python_to_cf, and field_types mappings,
        or None if not found.
    """
    _build_property_type_map()
    return _PROPERTY_TYPE_MAP.get((module, class_name))


def find_property_type_for_cf_keys(
    cf_keys: set[str], module_hint: Optional[str] = None
) -> Optional[tuple[str, str]]:
    """
    Find a PropertyType class that matches a set of CloudFormation property keys.

    Args:
        cf_keys: Set of CloudFormation property names from a dict
        module_hint: Optional module name to prefer (e.g., "s3").
                     If provided, ONLY matches from that module are considered.

    Returns:
        Tuple of (module_name, class_name) or None if no match.
    """
    _build_property_type_map()

    # Find candidates that have at least one matching key
    candidates: dict[tuple[str, str], int] = {}
    for key in cf_keys:
        if key in _CF_PROPERTY_TO_CLASSES:
            for class_key in _CF_PROPERTY_TO_CLASSES[key]:
                # If we have a module hint, skip classes from other modules
                # Use startswith to support nested modules (e.g., hint='ec2' matches 'ec2.instance')
                if module_hint and not class_key[0].startswith(module_hint):
                    continue
                candidates[class_key] = candidates.get(class_key, 0) + 1

    if not candidates:
        return None

    # Score candidates: prefer classes where ALL provided keys are valid
    best_matches: list[tuple[tuple[str, str], float, int]] = []
    for class_key, match_count in candidates.items():
        info = _PROPERTY_TYPE_MAP[class_key]
        total_keys = len(info["cf_to_python"])
        expected_keys = set(info["cf_to_python"].keys())

        # Check if all provided keys are in the expected set
        all_match = cf_keys.issubset(expected_keys)
        if not all_match:
            # Penalize partial matches heavily
            continue

        # Score: ratio of matched keys to total keys (higher is better, more specific)
        specificity = match_count / total_keys if total_keys > 0 else 0
        best_matches.append((class_key, specificity, total_keys))

    if not best_matches:
        return None

    # Sort by specificity desc (prefer more specific matches)
    best_matches.sort(key=lambda x: (-x[1], x[2]))

    return best_matches[0][0] if best_matches else None


def get_all_property_types() -> dict[tuple[str, str], dict[str, Any]]:
    """Get all known PropertyType classes and their information."""
    _build_property_type_map()
    return _PROPERTY_TYPE_MAP.copy()


# =============================================================================
# Ambiguous Class Name Detection
# =============================================================================

# Cache for class names that exist in multiple AWS modules
# Structure: {class_name: [list of module names]}
_CLASS_TO_MODULES: dict[str, list[str]] = {}
_CLASS_TO_MODULES_BUILT = False


def _build_class_to_modules_map() -> None:
    """Build mapping of class names to their modules for collision detection.

    Only classes in __init__.py are tracked (Resources), since PropertyTypes
    in submodules use qualified access (ec2.instance.NetworkInterface).
    """
    global _CLASS_TO_MODULES, _CLASS_TO_MODULES_BUILT
    if _CLASS_TO_MODULES_BUILT:
        return

    def scan_for_class_names(path: Path, module_name: str, content: str) -> None:
        """Extract class names from file content."""
        for match in CLASS_NAME_PATTERN.finditer(content):
            class_name = match.group(1)
            if class_name not in _CLASS_TO_MODULES:
                _CLASS_TO_MODULES[class_name] = []
            _CLASS_TO_MODULES[class_name].append(module_name)

    # Only scan __init__.py (nested) or flat .py files (legacy) - not submodules
    _scan_aws_modules(
        on_init_file=scan_for_class_names,
        on_flat_file=scan_for_class_names,
    )

    _CLASS_TO_MODULES_BUILT = True


def is_ambiguous_class_name(class_name: str) -> bool:
    """
    Check if a class name exists in multiple AWS modules.

    This is used during code generation to determine if we need to use
    qualified imports (e.g., iot.Policy) vs direct imports (e.g., Policy).

    Args:
        class_name: The class name to check (e.g., "Policy", "Function")

    Returns:
        True if the class name exists in more than one AWS module.
    """
    _build_class_to_modules_map()
    modules = _CLASS_TO_MODULES.get(class_name, [])
    return len(modules) > 1


def get_class_modules(class_name: str) -> list[str]:
    """
    Get all AWS modules that define a class with the given name.

    Args:
        class_name: The class name to check

    Returns:
        List of module names (e.g., ["iam", "iot"] for "Policy")
    """
    _build_class_to_modules_map()
    return _CLASS_TO_MODULES.get(class_name, [])
