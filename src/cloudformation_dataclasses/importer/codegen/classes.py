"""Class generation functions for CloudFormation elements.

This module generates Python dataclass definitions for CloudFormation
template elements:

- generate_parameter_class(): Parameter wrapper classes
- generate_resource_class(): Resource wrapper classes with properties
- generate_output_class(): Output wrapper classes
- generate_condition_class(): Condition wrapper classes
- generate_mapping_class(): Mapping wrapper classes

Each function takes an IR element and a CodegenContext, returning
Python source code as a string.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from cloudformation_dataclasses.constants import (
    PARAMETER_TYPE_MAP,
    is_ambiguous_class_name,
    resolve_resource_type,
)
from cloudformation_dataclasses.importer.ir import (
    IRCondition,
    IRMapping,
    IROutput,
    IRParameter,
    IRResource,
)

from .blocks import property_value_to_python_block
from .context import AnnotatedValue
from .helpers import sanitize_class_name, tag_class_name
from .values import escape_docstring, escape_string, value_to_python

if TYPE_CHECKING:
    from .context import CodegenContext


# =============================================================================
# Parameter Class Generation
# =============================================================================


def generate_parameter_class(param: IRParameter, ctx: "CodegenContext") -> str:
    """Generate a Parameter wrapper class definition.

    Creates a @cloudformation_dataclass with resource: Parameter annotation
    and all parameter properties (type, default, constraints, etc.).

    Args:
        param: The parsed IR parameter.
        ctx: Code generation context for import tracking.

    Returns:
        Python class definition as a string.
    """
    lines = []

    # Docstring
    if ctx.include_docstrings and param.description:
        lines.append(f'    {escape_docstring(param.description)}')
        lines.append("")

    # Resource type annotation
    ctx.add_import("cloudformation_dataclasses.core", "Parameter")
    lines.append("    resource: Parameter")

    # Type - use constant if available
    if param.type in PARAMETER_TYPE_MAP:
        const_name = PARAMETER_TYPE_MAP[param.type]
        ctx.add_parameter_type_import(const_name)
        lines.append(f"    type = {const_name}")
    else:
        lines.append(f"    type = {escape_string(param.type)}")

    # Optional fields
    if param.description:
        lines.append(f"    description = {escape_string(param.description)}")
    if param.default is not None:
        lines.append(f"    default = {value_to_python(param.default, ctx)}")
    if param.allowed_values:
        lines.append(f"    allowed_values = {value_to_python(param.allowed_values, ctx)}")
    if param.allowed_pattern:
        lines.append(f"    allowed_pattern = {escape_string(param.allowed_pattern)}")
    if param.min_length is not None:
        lines.append(f"    min_length = {param.min_length}")
    if param.max_length is not None:
        lines.append(f"    max_length = {param.max_length}")
    if param.min_value is not None:
        lines.append(f"    min_value = {param.min_value}")
    if param.max_value is not None:
        lines.append(f"    max_value = {param.max_value}")
    if param.constraint_description:
        lines.append(f"    constraint_description = {escape_string(param.constraint_description)}")
    if param.no_echo:
        lines.append("    no_echo = True")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    class_name = sanitize_class_name(param.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)


# =============================================================================
# Resource Class Generation
# =============================================================================


def generate_resource_class(resource: IRResource, ctx: "CodegenContext") -> str:
    """Generate a resource wrapper class."""
    # Set current resource ID to avoid self-referential ref() replacements
    ctx.current_resource_id = resource.logical_id
    lines = []

    # Docstring
    if ctx.include_docstrings:
        lines.append(f'    """{resource.resource_type} resource."""')
        lines.append("")

    # Resolve resource type
    resolved = resolve_resource_type(resource.resource_type)
    resource_module = None
    resource_field_types: dict[str, str] = {}

    if resolved:
        module, class_name = resolved
        resource_module = module
        ctx.current_module = module

        # Check if we need qualified name to avoid collisions:
        # 1. Wrapper class name matches AWS resource class name (e.g., class Policy uses iot.Policy)
        # 2. Class name exists in multiple AWS modules (e.g., Policy in both iam and iot)
        needs_qualified = (
            resource.logical_id == class_name
            or class_name in ctx.colliding_aws_names
            or is_ambiguous_class_name(class_name)
        )
        if needs_qualified:
            # Use module-qualified name: resource: iot.Policy instead of resource: Policy
            ctx.add_import("cloudformation_dataclasses.aws", module)
            lines.append(f"    resource: {module}.{class_name}")
        else:
            ctx.add_import(f"cloudformation_dataclasses.aws.{module}", class_name)
            lines.append(f"    resource: {class_name}")

        # Get field type information for this resource class
        # We need to scan the resource class for _property_mappings and field types
        try:
            import cloudformation_dataclasses.aws as aws_pkg
            from pathlib import Path
            aws_dir = Path(aws_pkg.__file__).parent

            # Handle both flat modules (aws/s3.py) and nested packages (aws/ec2/__init__.py)
            py_file = aws_dir / f"{module}.py"
            if not py_file.exists():
                # Try nested package
                py_file = aws_dir / module / "__init__.py"

            if py_file.exists():
                content = py_file.read_text()
                # Find the resource class and its field types
                in_target_class = False
                for line in content.split("\n"):
                    if f"class {class_name}(" in line:
                        in_target_class = True
                        continue
                    if in_target_class:
                        if line.startswith("class ") and f"class {class_name}(" not in line:
                            break  # Hit another class
                        # Look for field type annotations
                        field_match = re.match(r"^\s+(\w+):\s*(.+?)\s*(?:=|$)", line)
                        if field_match:
                            field_name, type_annotation = field_match.groups()
                            if not field_name.startswith("_"):
                                resource_field_types[field_name] = type_annotation
        except Exception:
            pass  # Continue without field types
    else:
        # Unknown resource type - use comment
        lines.append(f"    # Unknown resource type: {resource.resource_type}")
        lines.append("    resource: CloudFormationResource")
        ctx.add_import("cloudformation_dataclasses.core", "CloudFormationResource")

    # Properties - use block mode converter to generate PropertyType wrapper classes
    for prop in resource.properties.values():
        # Get the expected type for this property
        expected_type = resource_field_types.get(prop.python_name)

        value_result = property_value_to_python_block(
            prop.value,
            resource.logical_id,
            prop.python_name,
            expected_type,
            resource_module,
            ctx,
        )
        if isinstance(value_result, AnnotatedValue):
            # Annotation-based ref: bucket: Ref[Bucket] = ref()
            lines.append(f"    {prop.python_name}: {value_result.annotation} = {value_result.value}")
        else:
            lines.append(f"    {prop.python_name} = {value_result}")

    # Resource-level attributes
    if resource.depends_on:
        deps = ", ".join(f'"{d}"' for d in resource.depends_on)
        lines.append(f"    depends_on = [{deps}]")
    if resource.condition:
        lines.append(f"    condition = {escape_string(resource.condition)}")
    if resource.deletion_policy:
        lines.append(f"    deletion_policy = {escape_string(resource.deletion_policy)}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    class_name = sanitize_class_name(resource.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)


# =============================================================================
# Output Class Generation
# =============================================================================


def generate_output_class(output: IROutput, ctx: "CodegenContext") -> str:
    """Generate an output wrapper class."""
    lines = []

    # Docstring
    if ctx.include_docstrings and output.description:
        lines.append(f'    {escape_docstring(output.description)}')
        lines.append("")

    ctx.add_import("cloudformation_dataclasses.core", "Output")
    lines.append("    resource: Output")

    # Value
    value_str = value_to_python(output.value, ctx, indent=1)
    lines.append(f"    value = {value_str}")

    # Optional fields
    if output.description:
        lines.append(f"    description = {escape_string(output.description)}")
    if output.export_name:
        export_str = value_to_python(output.export_name, ctx, indent=1)
        lines.append(f"    export_name = {export_str}")
    if output.condition:
        lines.append(f"    condition = {escape_string(output.condition)}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    class_name = sanitize_class_name(output.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}Output:\n" + "\n".join(lines)


# =============================================================================
# Mapping Class Generation
# =============================================================================


def generate_mapping_class(mapping: IRMapping, ctx: "CodegenContext") -> str:
    """Generate a mapping wrapper class."""
    lines = []

    ctx.add_import("cloudformation_dataclasses.core", "Mapping")
    lines.append("    resource: Mapping")

    # Map data as dict - disable PropertyType keys since mapping data is user-defined
    map_str = value_to_python(mapping.map_data, ctx, indent=1, use_property_type_keys=False)
    lines.append(f"    map_data = {map_str}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    class_name = sanitize_class_name(mapping.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}Mapping:\n" + "\n".join(lines)


# =============================================================================
# Condition Class Generation
# =============================================================================


def generate_condition_class(condition: IRCondition, ctx: "CodegenContext") -> str:
    """Generate a condition wrapper class."""
    lines = []

    ctx.add_import("cloudformation_dataclasses.core", "Condition")
    lines.append("    resource: Condition")

    # Expression
    expr_str = value_to_python(condition.expression, ctx, indent=1)
    lines.append(f"    expression = {expr_str}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    class_name = sanitize_class_name(condition.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}Condition:\n" + "\n".join(lines)


# =============================================================================
# Tag Class Generation
# =============================================================================


def generate_tag_class(key: str, value: str, ctx: "CodegenContext") -> str:
    """Generate a tag wrapper class for mixed mode."""
    lines = []
    class_name = tag_class_name(key, value)

    ctx.add_import("cloudformation_dataclasses.core", "Tag")
    lines.append("    resource: Tag")
    lines.append(f"    key = {escape_string(key)}")
    lines.append(f"    value = {escape_string(value)}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)
