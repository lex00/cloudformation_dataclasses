"""
CloudFormation resource class generator.

This module generates Python dataclasses from CloudFormation Resource Specifications.
It converts AWS resource types to type-safe Python classes with proper type annotations.

Structure:
    Each AWS service becomes a package (e.g., ec2/) containing:
    - __init__.py: Resource classes and submodule imports
    - {resource}.py: PropertyTypes for each resource (e.g., instance.py, bucket.py)

    This mirrors CloudFormation's type hierarchy:
    - AWS::EC2::Instance -> ec2.Instance
    - AWS::EC2::Instance.NetworkInterface -> ec2.instance.NetworkInterface
"""

from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

from cloudformation_dataclasses.codegen.config import (
    CLOUDFORMATION_SPEC_VERSION,
    GENERATOR_VERSION,
    COMBINED_VERSION,
)

from cloudformation_dataclasses.codegen.botocore_enums import (
    generate_service_enums,
    get_property_enum_mappings,
    CLASS_ALIASES,
    CF_TO_BOTOCORE_STRUCT,
)
from cloudformation_dataclasses.codegen.spec_parser import (
    CloudFormationSpec,
    PropertySpec,
    PropertyTypeSpec,
    ResourceSpec,
    get_spec,
)


def to_snake_case(name: str) -> str:
    """
    Convert PascalCase to snake_case.

    Examples:
        BucketName -> bucket_name
        VPCId -> vpc_id
        S3Key -> s3_key
        IPv6CidrBlock -> ipv6_cidr_block
    """
    # Insert underscore before uppercase letters (except at start)
    result = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Insert underscore before uppercase in acronyms
    result = re.sub("([a-z0-9])([A-Z])", r"\1_\2", result)
    return result.lower()


def sanitize_python_name(name: str) -> str:
    """
    Sanitize names to be valid Python identifiers.

    If name conflicts with Python keywords, append underscore.
    """
    python_keywords = {
        "and",
        "as",
        "assert",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
        "type",
    }

    if name in python_keywords:
        return f"{name}_"
    return name


def map_primitive_type(primitive_type: str) -> str:
    """
    Map CloudFormation primitive types to Python types.

    Args:
        primitive_type: CloudFormation primitive type (String, Integer, Boolean, etc.)

    Returns:
        Python type annotation string
    """
    type_mapping = {
        "String": "str",
        "Integer": "int",
        "Long": "int",
        "Double": "float",
        "Boolean": "bool",
        "Json": "dict[str, Any]",
        "Timestamp": "str",  # ISO 8601 timestamp string
    }
    return type_mapping.get(primitive_type, "Any")


def map_property_type(
    prop: PropertySpec,
    resource_type: str,
    prop_name: str | None = None,
    struct_name: str | None = None,
    enum_mappings: dict[tuple[str, str], str] | None = None,
    submodule_name: str | None = None,
) -> str:
    """
    Map a CloudFormation property to a Python type annotation.

    Args:
        prop: Property specification
        resource_type: The resource type this property belongs to
        prop_name: Original CloudFormation property name (for enum lookup)
        struct_name: Structure name (for enum lookup, e.g., "KeySchema")
        enum_mappings: Dict mapping (struct_name, prop_name) to enum type
        submodule_name: If set, prefix PropertyType references with this submodule

    Returns:
        Python type annotation string with intrinsic function support
    """
    # Handle primitive types
    if prop.primitive_type:
        base_type = map_primitive_type(prop.primitive_type)

        # Check if this property maps to an enum type
        if prop.primitive_type == "String" and enum_mappings and struct_name and prop_name:
            # Try direct lookup first
            enum_type = enum_mappings.get((struct_name, prop_name))

            # If not found, try mapping CF struct name to botocore struct name
            if not enum_type:
                botocore_struct = CF_TO_BOTOCORE_STRUCT.get(struct_name)
                if botocore_struct:
                    enum_type = enum_mappings.get((botocore_struct, prop_name))

            if enum_type:
                # Apply class alias if defined (e.g., ScalarAttributeType -> AttributeType)
                display_type = CLASS_ALIASES.get(enum_type, enum_type)
                return f"Union[str, {display_type}, Ref, GetAtt, Sub]"

        # Add intrinsic function support
        return f"Union[{base_type}, Ref, GetAtt, Sub]"

    # Handle List types
    if prop.type == "List":
        if prop.primitive_item_type:
            item_type = map_primitive_type(prop.primitive_item_type)
            return f"Union[list[{item_type}], Ref]"
        elif prop.item_type:
            # Complex item type (property type class)
            item_name = prop.item_type
            if submodule_name:
                return f"list[{submodule_name}.{item_name}]"
            return f"list[{item_name}]"
        else:
            return "Union[list[Any], Ref]"

    # Handle Map types
    if prop.type == "Map":
        if prop.primitive_item_type:
            value_type = map_primitive_type(prop.primitive_item_type)
            return f"dict[str, {value_type}]"
        else:
            return "dict[str, Any]"

    # Handle property type references (nested structures)
    if prop.type:
        # The type is a property type class name
        simple_name = prop.type.split(".")[-1]  # Get last part after "."
        if submodule_name:
            return f"{submodule_name}.{simple_name}"
        return simple_name

    # Fallback
    return "Any"


def generate_property_type_class(
    prop_type: PropertyTypeSpec,
    indent: str = "",
    enum_mappings: dict[tuple[str, str], str] | None = None,
) -> str:
    """
    Generate a dataclass for a CloudFormation property type.

    Args:
        prop_type: Property type specification
        indent: Indentation string for nested classes
        enum_mappings: Dict mapping (struct_name, prop_name) to enum type

    Returns:
        Generated Python dataclass code
    """
    simple_name = prop_type.simple_name
    lines = []

    # Class definition - inherit from PropertyType for data-driven serialization
    lines.append(f"{indent}@dataclass")
    lines.append(f"{indent}class {simple_name}(PropertyType):")

    # Generate properties
    if not prop_type.properties:
        lines.append(f"{indent}    pass")
    else:
        # Generate CloudFormation property name constants
        # These allow type-safe dict key access: PropertyType.FIELD_NAME
        for prop_name, prop in prop_type.properties.items():
            const_name = to_snake_case(prop_name).upper()
            lines.append(f'{indent}    {const_name} = "{prop_name}"')
        lines.append("")

        # Generate _property_mappings for data-driven serialization
        lines.append(f"{indent}    _property_mappings: ClassVar[dict[str, str]] = {{")
        for prop_name, prop in prop_type.properties.items():
            snake_name = sanitize_python_name(to_snake_case(prop_name))
            lines.append(f'{indent}        "{snake_name}": "{prop_name}",')
        lines.append(f"{indent}    }}")
        lines.append("")

        for prop_name, prop in prop_type.properties.items():
            snake_name = sanitize_python_name(to_snake_case(prop_name))
            python_type = map_property_type(
                prop,
                prop_type.type_name,
                prop_name=prop_name,
                struct_name=simple_name,
                enum_mappings=enum_mappings,
            )

            # Add field - make all optional for consistency
            lines.append(f"{indent}    {snake_name}: Optional[{python_type}] = None")

    # Note: _serialize_value() and to_dict() are inherited from PropertyType base class

    return "\n".join(lines)


def generate_resource_class_only(
    resource: ResourceSpec,
    enum_mappings: dict[tuple[str, str], str] | None = None,
    submodule_name: str | None = None,
) -> str:
    """
    Generate a dataclass for a CloudFormation resource (without inline PropertyTypes).

    Args:
        resource: Resource specification
        enum_mappings: Dict mapping (struct_name, prop_name) to enum type
        submodule_name: Submodule name for PropertyType references (e.g., "instance")

    Returns:
        Generated Python dataclass code
    """
    class_name = resource.class_name
    lines = []

    # Resource class definition
    lines.append("@dataclass")
    lines.append(f"class {class_name}(CloudFormationResource):")

    # Docstring
    doc = (
        resource.documentation.split("\n")[0][:80]
        if resource.documentation
        else resource.resource_type
    )
    lines.append(f'    """{doc}"""')
    lines.append("")

    # Resource type constant
    lines.append(f'    resource_type: ClassVar[str] = "{resource.resource_type}"')

    # Generate properties
    if not resource.properties:
        lines.append("")
        lines.append("    pass")
    else:
        # Generate CloudFormation property name constants
        # These allow type-safe dict key access: Resource.FIELD_NAME
        for prop_name, prop in resource.properties.items():
            const_name = to_snake_case(prop_name).upper()
            lines.append(f'    {const_name} = "{prop_name}"')
        lines.append("")

        # Generate _property_mappings for data-driven serialization
        lines.append("    _property_mappings: ClassVar[dict[str, str]] = {")
        for prop_name, prop in resource.properties.items():
            snake_name = sanitize_python_name(to_snake_case(prop_name))
            lines.append(f'        "{snake_name}": "{prop_name}",')
        lines.append("    }")
        lines.append("")

        for prop_name, prop in resource.properties.items():
            snake_name = sanitize_python_name(to_snake_case(prop_name))
            python_type = map_property_type(
                prop,
                resource.resource_type,
                prop_name=prop_name,
                struct_name=class_name,
                enum_mappings=enum_mappings,
                submodule_name=submodule_name,
            )

            # Add field - make all optional to avoid dataclass inheritance issues
            # Even "required" fields can be optional in wrapper dataclasses
            lines.append(f"    {snake_name}: Optional[{python_type}] = None")

    # Generate typed attribute accessors
    if resource.attributes:
        lines.append("")
        for attr_name, attr_spec in resource.attributes.items():
            # Replace dots with underscores for Python method names
            snake_name = to_snake_case(attr_name.replace(".", "_"))
            lines.append("    @property")
            lines.append(f"    def attr_{snake_name}(self) -> GetAtt:")
            lines.append(f'        """Get the {attr_name} attribute."""')
            lines.append(f'        return self.get_att("{attr_name}")')
            lines.append("")

    return "\n".join(lines)


def _generate_module_header(service: str) -> str:
    """Generate module docstring with version metadata."""
    lines = [
        '"""',
        f"AWS CloudFormation {service} Resources",
        "",
        "⚠️  AUTO-GENERATED FILE - DO NOT EDIT MANUALLY ⚠️",
        "",
        "This file is automatically generated from the AWS CloudFormation Resource Specification.",
        "Any manual changes will be overwritten when regenerated.",
        "",
        "Version Information:",
        f"  CloudFormation Spec: {CLOUDFORMATION_SPEC_VERSION}",
        f"  Generator Version: {GENERATOR_VERSION}",
        f"  Combined: {COMBINED_VERSION}",
        f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "To regenerate:",
        f"    uv run python -m cloudformation_dataclasses.codegen.generator --service {service}",
        '"""',
    ]
    return "\n".join(lines)


def _generate_common_imports() -> str:
    """Generate common import statements."""
    lines = [
        "",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from typing import Any, ClassVar, Optional, Union",
        "",
        "from cloudformation_dataclasses.core.base import CloudFormationResource, PropertyType, Tag",
        "from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub",
    ]
    return "\n".join(lines)


def _generate_property_type_imports() -> str:
    """Generate imports for PropertyType submodules."""
    lines = [
        "",
        "from __future__ import annotations",
        "",
        "from dataclasses import dataclass",
        "from typing import Any, ClassVar, Optional, Union",
        "",
        "from cloudformation_dataclasses.core.base import PropertyType, Tag",
        "from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub",
    ]
    return "\n".join(lines)


def _generate_property_type_module(
    path: Path,
    resource_spec: ResourceSpec,
    prop_types: dict[str, PropertyTypeSpec],
    enum_mappings: dict[tuple[str, str], str] | None,
    enum_classes: str | None,
) -> None:
    """Generate a module containing PropertyTypes for a single resource."""
    lines = [
        f'"""PropertyTypes for {resource_spec.resource_type}."""',
        _generate_property_type_imports(),
    ]

    # Include enum classes if they reference types used in this module
    if enum_classes:
        lines.append("")
        lines.append("")
        lines.append("# Service Constants (auto-generated from botocore)")
        lines.append(enum_classes)

    lines.append("")
    lines.append("")

    for prop_type in prop_types.values():
        lines.append(generate_property_type_class(prop_type, enum_mappings=enum_mappings))
        lines.append("")
        lines.append("")

    with open(path, "w") as f:
        f.write("\n".join(lines))


def generate_service_package(
    service: str,
    spec: CloudFormationSpec,
    output_dir: Path,
) -> Path:
    """
    Generate a package directory for an AWS service.

    Creates:
      - {service}/__init__.py with Resource classes
      - {service}/{resource}.py for each resource's PropertyTypes

    Args:
        service: Service name (e.g., "S3", "EC2")
        spec: CloudFormation specification
        output_dir: Output directory for generated files

    Returns:
        Path to generated package directory
    """
    service_lower = service.lower()
    if service_lower == "lambda":
        package_name = "lambda_"
    else:
        package_name = service_lower

    package_dir = output_dir / package_name

    # Clean existing package if it exists
    if package_dir.exists():
        shutil.rmtree(package_dir)

    package_dir.mkdir(parents=True, exist_ok=True)

    # Get all resources for this service
    resources = spec.get_resources_by_service(service)

    if not resources:
        print(f"Warning: No resources found for service: {service}")
        return package_dir

    # Generate enum constants (shared across package)
    enum_classes, enum_aliases = generate_service_enums(service)
    enum_mappings = get_property_enum_mappings(service)

    # Build __init__.py content
    init_lines = [_generate_module_header(service)]
    init_lines.append(_generate_common_imports())

    # Track submodules to import
    submodules = []

    # Process each resource
    resource_classes = []
    for resource_type, resource_spec in resources.items():
        resource_name = resource_spec.class_name  # e.g., "Instance"
        resource_name_lower = to_snake_case(resource_name)  # e.g., "instance"

        # Check if this resource has PropertyTypes
        prop_types = spec.get_property_types_for_resource(resource_type)

        if prop_types:
            # Generate submodule for PropertyTypes
            submodule_path = package_dir / f"{resource_name_lower}.py"
            _generate_property_type_module(
                submodule_path, resource_spec, prop_types, enum_mappings, enum_classes
            )
            submodules.append(resource_name_lower)

            # Generate Resource class with submodule references
            resource_classes.append(
                generate_resource_class_only(
                    resource_spec,
                    enum_mappings=enum_mappings,
                    submodule_name=resource_name_lower,
                )
            )
        else:
            # No PropertyTypes - generate Resource class without submodule reference
            resource_classes.append(
                generate_resource_class_only(resource_spec, enum_mappings=enum_mappings)
            )

    # Add enum classes to __init__.py
    if enum_classes:
        init_lines.append("")
        init_lines.append("")
        init_lines.append("# " + "=" * 77)
        init_lines.append("# Service Constants (auto-generated from botocore)")
        init_lines.append("# " + "=" * 77)
        init_lines.append("")
        init_lines.append(enum_classes)
        init_lines.append("")
        init_lines.append("")
        init_lines.append("# Convenient aliases for enum values")
        init_lines.append(enum_aliases)

    # Add submodule imports
    if submodules:
        init_lines.append("")
        init_lines.append("")
        init_lines.append("# PropertyType submodules (e.g., ec2.instance.NetworkInterface)")
        for submod in sorted(set(submodules)):
            init_lines.append(f"from . import {submod}")

    init_lines.append("")
    init_lines.append("")

    # Add resource classes
    for resource_class in resource_classes:
        init_lines.append(resource_class)
        init_lines.append("")
        init_lines.append("")

    # Write __init__.py
    with open(package_dir / "__init__.py", "w") as f:
        f.write("\n".join(init_lines))

    print(f"✅ Generated {len(resources)} resources for {service} -> {package_dir}/")
    return package_dir


if __name__ == "__main__":
    """CLI for generating resource classes."""
    import sys

    # Parse arguments
    if "--service" in sys.argv:
        # Generate single service
        idx = sys.argv.index("--service")
        service = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else None

        if not service:
            print("Error: --service requires a service name")
            sys.exit(1)

        print(f"Generating classes for service: {service}")
        spec = get_spec()
        output_dir = Path("src/cloudformation_dataclasses/aws")
        generate_service_package(service, spec, output_dir)

    elif "--all" in sys.argv:
        # Generate all services
        print("Generating classes for all services...")
        spec = get_spec()
        output_dir = Path("src/cloudformation_dataclasses/aws")

        services = spec.list_services()
        print(f"Found {len(services)} services")

        for service in services:
            try:
                generate_service_package(service, spec, output_dir)
            except Exception as e:
                print(f"❌ Error generating {service}: {e}")

        print("\n✅ Generation complete!")

    else:
        print("CloudFormation Resource Generator")
        print("\nUsage:")
        print("  python -m cloudformation_dataclasses.codegen.generator --service S3")
        print("  python -m cloudformation_dataclasses.codegen.generator --all")
