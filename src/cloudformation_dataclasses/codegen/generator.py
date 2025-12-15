"""
CloudFormation resource class generator.

This module generates Python dataclasses from CloudFormation Resource Specifications.
It converts AWS resource types to type-safe Python classes with proper type annotations.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Any

from cloudformation_dataclasses.codegen.config import (
    CLOUDFORMATION_SPEC_VERSION,
    GENERATOR_VERSION,
    COMBINED_VERSION,
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


def map_property_type(prop: PropertySpec, resource_type: str) -> str:
    """
    Map a CloudFormation property to a Python type annotation.

    Args:
        prop: Property specification
        resource_type: The resource type this property belongs to

    Returns:
        Python type annotation string with intrinsic function support
    """
    # Handle primitive types
    if prop.primitive_type:
        base_type = map_primitive_type(prop.primitive_type)
        # Add intrinsic function support
        return f"Union[{base_type}, Ref, GetAtt, Sub]"

    # Handle List types
    if prop.type == "List":
        if prop.primitive_item_type:
            item_type = map_primitive_type(prop.primitive_item_type)
            return f"Union[list[{item_type}], Ref]"
        elif prop.item_type:
            # Complex item type (property type class)
            return f"list[{prop.item_type}]"
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
        return simple_name

    # Fallback
    return "Any"


def generate_property_type_class(
    prop_type: PropertyTypeSpec, indent: str = ""
) -> str:
    """
    Generate a dataclass for a CloudFormation property type.

    Args:
        prop_type: Property type specification
        indent: Indentation string for nested classes

    Returns:
        Generated Python dataclass code
    """
    simple_name = prop_type.simple_name
    lines = []

    # Class definition
    lines.append(f"{indent}@dataclass")
    lines.append(f"{indent}class {simple_name}:")

    # Docstring
    if prop_type.documentation:
        doc = prop_type.documentation.split("\n")[0][:80]  # First line, truncated
        lines.append(f'{indent}    """{doc}"""')
        lines.append("")

    # Generate properties
    if not prop_type.properties:
        lines.append(f"{indent}    pass")
    else:
        for prop_name, prop in prop_type.properties.items():
            snake_name = sanitize_python_name(to_snake_case(prop_name))
            python_type = map_property_type(prop, prop_type.type_name)

            # Add comment if documentation exists
            if prop.documentation:
                doc_line = prop.documentation.split("\n")[0][:60]
                lines.append(f"{indent}    # {doc_line}")

            # Add field - make all optional for consistency
            lines.append(f"{indent}    {snake_name}: Optional[{python_type}] = None")

    # Add to_dict() method for CloudFormation serialization
    if prop_type.properties:
        lines.append("")
        lines.append(f"{indent}    def to_dict(self) -> dict[str, Any]:")
        lines.append(f'{indent}        """Serialize to CloudFormation format."""')
        lines.append(f"{indent}        props: dict[str, Any] = {{}}")
        lines.append("")

        for prop_name, prop in prop_type.properties.items():
            snake_name = sanitize_python_name(to_snake_case(prop_name))
            lines.append(f"{indent}        if self.{snake_name} is not None:")
            lines.append(f"{indent}            if hasattr(self.{snake_name}, 'to_dict'):")
            lines.append(f"{indent}                props['{prop_name}'] = self.{snake_name}.to_dict()")
            lines.append(f"{indent}            elif isinstance(self.{snake_name}, list):")
            lines.append(f"{indent}                props['{prop_name}'] = [")
            lines.append(f"{indent}                    item.to_dict() if hasattr(item, 'to_dict') else item")
            lines.append(f"{indent}                    for item in self.{snake_name}")
            lines.append(f"{indent}                ]")
            lines.append(f"{indent}            else:")
            lines.append(f"{indent}                props['{prop_name}'] = self.{snake_name}")
            lines.append("")

        lines.append(f"{indent}        return props")

    return "\n".join(lines)


def generate_resource_class(resource: ResourceSpec, spec: CloudFormationSpec) -> str:
    """
    Generate a dataclass for a CloudFormation resource.

    Args:
        resource: Resource specification
        spec: Full CloudFormation spec (for looking up property types)

    Returns:
        Generated Python dataclass code
    """
    class_name = resource.class_name
    lines = []

    # Generate property type classes first
    prop_types = spec.get_property_types_for_resource(resource.resource_type)
    for prop_type in prop_types.values():
        lines.append(generate_property_type_class(prop_type))
        lines.append("\n")

    # Resource class definition
    lines.append("@dataclass")
    lines.append(f"class {class_name}(CloudFormationResource):")

    # Docstring
    doc = resource.documentation.split("\n")[0][:80] if resource.documentation else resource.resource_type
    lines.append(f'    """{doc}"""')
    lines.append("")

    # Resource type constant
    lines.append(f'    resource_type: ClassVar[str] = "{resource.resource_type}"')
    lines.append("")

    # Generate properties
    if not resource.properties:
        lines.append("    pass")
    else:
        for prop_name, prop in resource.properties.items():
            snake_name = sanitize_python_name(to_snake_case(prop_name))
            python_type = map_property_type(prop, resource.resource_type)

            # Add comment
            if prop.documentation:
                doc_line = prop.documentation.split("\n")[0][:70]
                lines.append(f"    # {doc_line}")

            # Add field - make all optional to avoid dataclass inheritance issues
            # Even "required" fields can be optional in wrapper dataclasses
            lines.append(f"    {snake_name}: Optional[{python_type}] = None")

        lines.append("")

        # Implement _get_properties
        lines.append("    def _get_properties(self) -> dict[str, Any]:")
        lines.append('        """Serialize resource properties to CloudFormation format."""')
        lines.append("        props: dict[str, Any] = {}")
        lines.append("")

        for prop_name, prop in resource.properties.items():
            snake_name = sanitize_python_name(to_snake_case(prop_name))

            # Special case for Tags - use all_tags to include context tags
            if snake_name == "tags":
                lines.append(f"        # Serialize tags - use all_tags to include context tags")
                lines.append(f"        merged_tags = self.all_tags")
                lines.append(f"        if merged_tags:")
                lines.append(f"            props['{prop_name}'] = [")
                lines.append(f"                item.to_dict() if hasattr(item, 'to_dict') else item")
                lines.append(f"                for item in merged_tags")
                lines.append(f"            ]")
                lines.append("")
            else:
                lines.append(f"        if self.{snake_name} is not None:")
                lines.append(f"            # Serialize {snake_name} (handle intrinsic functions)")
                lines.append(f"            if hasattr(self.{snake_name}, 'to_dict'):")
                lines.append(f'                props["{prop_name}"] = self.{snake_name}.to_dict()')
                lines.append(f"            elif isinstance(self.{snake_name}, list):")
                lines.append(f"                # Serialize list items (may contain intrinsic functions)")
                lines.append(f"                props['{prop_name}'] = [")
                lines.append(f"                    item.to_dict() if hasattr(item, 'to_dict') else item")
                lines.append(f"                    for item in self.{snake_name}")
                lines.append(f"                ]")
                lines.append(f"            else:")
                lines.append(f'                props["{prop_name}"] = self.{snake_name}')
                lines.append("")

        lines.append("        return props")

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


def generate_service_module(
    service: str,
    spec: CloudFormationSpec,
    output_dir: Path,
) -> Path:
    """
    Generate a complete module file for an AWS service.

    Args:
        service: Service name (e.g., "S3", "EC2")
        spec: CloudFormation specification
        output_dir: Output directory for generated files

    Returns:
        Path to generated module file

    Example:
        >>> spec = get_spec()
        >>> generate_service_module("S3", spec, Path("src/cloudformation_dataclasses/aws"))
    """
    service_lower = service.lower()
    if service_lower == "lambda":
        module_name = "lambda_"  # Avoid Python keyword
    else:
        module_name = service_lower

    output_file = output_dir / f"{module_name}.py"

    # Get all resources for this service
    resources = spec.get_resources_by_service(service)

    if not resources:
        print(f"Warning: No resources found for service: {service}")
        return output_file

    lines = []

    # Module header with version metadata
    lines.append(f'"""')
    lines.append(f"AWS CloudFormation {service} Resources")
    lines.append("")
    lines.append("⚠️  AUTO-GENERATED FILE - DO NOT EDIT MANUALLY ⚠️")
    lines.append("")
    lines.append("This file is automatically generated from the AWS CloudFormation Resource Specification.")
    lines.append("Any manual changes will be overwritten when regenerated.")
    lines.append("")
    lines.append("Version Information:")
    lines.append(f"  CloudFormation Spec: {spec.spec_version}")
    lines.append(f"  Generator Version: {GENERATOR_VERSION}")
    lines.append(f"  Combined: {COMBINED_VERSION}")
    lines.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("To regenerate this file:")
    lines.append(f"    uv run python -m cloudformation_dataclasses.codegen.generator --service {service}")
    lines.append('"""')
    lines.append("")

    # Imports
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from dataclasses import dataclass")
    lines.append("from typing import Any, ClassVar, Optional, Union")
    lines.append("")
    lines.append("from cloudformation_dataclasses.core.base import CloudFormationResource")
    lines.append("from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub")
    lines.append("")
    lines.append("")

    # Generate all resource classes
    for resource_type, resource_spec in resources.items():
        lines.append(generate_resource_class(resource_spec, spec))
        lines.append("\n\n")

    # Write to file
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w") as f:
        f.write("\n".join(lines))

    print(f"✅ Generated {len(resources)} resources for {service} -> {output_file}")
    return output_file


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
        generate_service_module(service, spec, output_dir)

    elif "--all" in sys.argv:
        # Generate all services
        print("Generating classes for all services...")
        spec = get_spec()
        output_dir = Path("src/cloudformation_dataclasses/aws")

        services = spec.list_services()
        print(f"Found {len(services)} services")

        for service in services:
            try:
                generate_service_module(service, spec, output_dir)
            except Exception as e:
                print(f"❌ Error generating {service}: {e}")

        print(f"\n✅ Generation complete!")

    else:
        print("CloudFormation Resource Generator")
        print("\nUsage:")
        print("  python -m cloudformation_dataclasses.codegen.generator --service S3")
        print("  python -m cloudformation_dataclasses.codegen.generator --all")
