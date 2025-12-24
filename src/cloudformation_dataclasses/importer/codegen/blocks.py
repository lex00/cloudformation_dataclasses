"""Block mode PropertyType wrapper generation."""

from __future__ import annotations

import datetime
import re
from typing import TYPE_CHECKING, Any, Optional

from cloudformation_dataclasses.constants import (
    CONDITION_OPERATOR_MAP,
    get_property_type_info,
    is_ambiguous_class_name,
)
from cloudformation_dataclasses.importer.ir import IRIntrinsic

from .context import AnnotatedValue
from .helpers import (
    extract_class_from_type_hint,
    resolve_property_type,
)
from .values import (
    annotated_to_class_ref,
    escape_string,
    intrinsic_to_python,
    try_convert_to_enum,
    value_to_python,
)

if TYPE_CHECKING:
    from .context import CodegenContext


# =============================================================================
# Block Mode Value Conversion
# =============================================================================


def property_value_to_python_block(
    value: Any,
    parent_logical_id: str,
    property_path: str,
    expected_type: Optional[str],
    expected_module: Optional[str],
    ctx: "CodegenContext",
) -> str | AnnotatedValue:
    """
    Convert a property value to Python code in block mode.

    For PropertyTypes: generates separate wrapper class, returns class name.
    For primitives/enums: returns literal value.
    For lists of PropertyTypes: returns [WrapperClassName].
    """
    if isinstance(value, IRIntrinsic):
        return intrinsic_to_python(value, ctx)

    if value is None:
        return "None"

    if isinstance(value, bool):
        return "True" if value else "False"

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        # Try enum conversion
        if expected_type:
            enum_ref = try_convert_to_enum(value, expected_type, ctx)
            if enum_ref:
                return enum_ref
        return escape_string(value)

    if isinstance(value, list):
        if not value:
            return "[]"

        # Extract inner type from list[...] annotation
        inner_class = None
        if expected_type:
            list_match = re.match(r".*list\[(\w+)\].*", expected_type, re.IGNORECASE)
            if list_match:
                inner_class = list_match.group(1)

        # Check if items are PropertyTypes
        items = []
        for i, item in enumerate(value):
            item_result = property_value_to_python_block(
                item,
                parent_logical_id,
                f"{property_path}.{i}",
                f"Optional[{inner_class}]" if inner_class else expected_type,
                expected_module,
                ctx,
            )
            # AnnotatedValue is only for top-level properties, not inside lists
            if isinstance(item_result, AnnotatedValue):
                item_str = annotated_to_class_ref(item_result)
            else:
                item_str = item_result
            items.append(item_str)

        if len(items) == 1:
            return f"[{items[0]}]"
        return "[" + ", ".join(items) + "]"

    if isinstance(value, dict):
        # Handle policy documents specially - generate PolicyDocument/PolicyStatement wrappers
        if _is_policy_document(value):
            return _generate_policy_document_wrapper_block(
                value, parent_logical_id, property_path, ctx
            )

        # Try to match to PropertyType
        expected_class = extract_class_from_type_hint(expected_type)
        cf_keys = set(value.keys())

        resolved = resolve_property_type(
            expected_class, expected_module, cf_keys, module_hint=expected_module
        )

        if resolved:
            pt_module, pt_class, _ = resolved
            class_name = generate_property_type_wrapper(
                value,
                parent_logical_id,
                property_path,
                pt_module,
                pt_class,
                ctx,
            )
            return class_name

        # Fall back to dict literal
        return value_to_python(value, ctx, indent=1)

    return repr(value)


# =============================================================================
# PropertyType Wrapper Generation
# =============================================================================


def generate_property_type_wrapper(
    value: dict[str, Any],
    parent_logical_id: str,
    property_path: str,
    pt_module: str,
    pt_class: str,
    ctx: "CodegenContext",
) -> str:
    """
    Generate a @cloudformation_dataclass wrapper for a PropertyType value.

    Returns the generated class name.
    """
    # Generate class name: {ParentLogicalId}{PropertyTypeName}
    class_name = f"{parent_logical_id}{pt_class}"

    # Handle name collisions by appending index
    if class_name in ctx.generated_classes:
        i = 1
        while f"{class_name}{i}" in ctx.generated_classes:
            i += 1
        class_name = f"{class_name}{i}"

    ctx.generated_classes.add(class_name)

    # Get PropertyType info for field mapping
    property_type_info = get_property_type_info(pt_module, pt_class)
    if not property_type_info:
        # Fallback if no info available - return as dict
        return value_to_python(value, ctx, indent=1)

    cf_to_python = property_type_info["cf_to_python"]
    field_types = property_type_info["field_types"]

    lines = []

    # Handle nested module paths (e.g., "ec2.instance" for PropertyTypes)
    if "." in pt_module:
        # Nested module: ec2.instance.NetworkInterface
        # Import base service: from cloudformation_dataclasses.aws import ec2
        base_module = pt_module.split(".")[0]
        ctx.add_import("cloudformation_dataclasses.aws", base_module)
        lines.append(f"    resource: {pt_module}.{pt_class}")
    elif is_ambiguous_class_name(pt_class):
        # Use qualified name: resource: s3.BucketEncryption
        ctx.add_import("cloudformation_dataclasses.aws", pt_module)
        lines.append(f"    resource: {pt_module}.{pt_class}")
    else:
        ctx.add_import(f"cloudformation_dataclasses.aws.{pt_module}", pt_class)
        lines.append(f"    resource: {pt_class}")

    # Convert each field
    for cf_key, val in value.items():
        if cf_key in cf_to_python:
            python_field = cf_to_python[cf_key]
            field_type = field_types.get(python_field)

            # Recursively handle nested PropertyTypes
            val_result = property_value_to_python_block(
                val,
                parent_logical_id,
                f"{property_path}.{python_field}",
                field_type,
                pt_module,
                ctx,
            )
            # Handle annotation-based refs for top-level properties
            if isinstance(val_result, AnnotatedValue):
                lines.append(f"    {python_field}: {val_result.annotation} = {val_result.value}")
            else:
                lines.append(f"    {python_field} = {val_result}")
        else:
            # Unknown key - still include it but as comment
            val_str = value_to_python(val, ctx, indent=1)
            # Comment out each line for multi-line values
            comment_lines = val_str.split("\n")
            if len(comment_lines) == 1:
                lines.append(f"    # Unknown CF key: {cf_key} = {val_str}")
            else:
                lines.append(f"    # Unknown CF key: {cf_key} = {comment_lines[0]}")
                for line in comment_lines[1:]:
                    lines.append(f"    # {line}")

    # Add import for decorator
    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    # Store class definition
    class_def = f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)
    ctx.property_type_class_defs.append(class_def)

    return class_name


# =============================================================================
# Policy Document/Statement Detection and Generation
# =============================================================================


def _is_policy_document(value: dict[str, Any]) -> bool:
    """Check if a dict looks like an IAM policy document."""
    return (
        isinstance(value, dict)
        and "Statement" in value
        and isinstance(value.get("Statement"), list)
    )


def _is_policy_statement(value: dict[str, Any]) -> bool:
    """Check if a dict looks like an IAM policy statement."""
    return (
        isinstance(value, dict) and "Effect" in value and value.get("Effect") in ("Allow", "Deny")
    )


def _generate_policy_statement_wrapper_block(
    stmt: dict[str, Any],
    parent_logical_id: str,
    property_path: str,
    stmt_index: int,
    ctx: "CodegenContext",
) -> str:
    """
    Generate a @cloudformation_dataclass wrapper for a PolicyStatement.

    Returns the generated class name.
    """
    # Generate class name based on effect and index
    effect = stmt.get("Effect", "Allow")
    base_name = "Deny" if effect == "Deny" else "Allow"
    class_name = f"{parent_logical_id}{base_name}Statement{stmt_index}"

    # Handle name collisions
    if class_name in ctx.generated_classes:
        i = 1
        while f"{class_name}_{i}" in ctx.generated_classes:
            i += 1
        class_name = f"{class_name}_{i}"

    ctx.generated_classes.add(class_name)

    # Add imports
    if effect == "Deny":
        ctx.add_import("cloudformation_dataclasses.core", "DenyStatement")
        base_class = "DenyStatement"
    else:
        ctx.add_import("cloudformation_dataclasses.core", "PolicyStatement")
        base_class = "PolicyStatement"
    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    lines = []
    lines.append(f"    resource: {base_class}")

    # Map statement fields to PolicyStatement attributes
    # Note: We use value_to_python here (not property_value_to_python_block)
    # because principal/action/resource are plain values, not PropertyTypes
    if "Sid" in stmt:
        lines.append(f"    sid = {escape_string(stmt['Sid'])}")

    if "Principal" in stmt:
        principal_str = value_to_python(stmt["Principal"], ctx, indent=1)
        lines.append(f"    principal = {principal_str}")

    if "Action" in stmt:
        action_str = value_to_python(stmt["Action"], ctx, indent=1)
        lines.append(f"    action = {action_str}")

    if "Resource" in stmt:
        resource_str = value_to_python(stmt["Resource"], ctx, indent=1)
        lines.append(f"    resource_arn = {resource_str}")

    if "Condition" in stmt:
        condition_str = condition_to_python(stmt["Condition"], ctx, indent=1)
        lines.append(f"    condition = {condition_str}")

    # Store class definition
    class_def = f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)
    ctx.property_type_class_defs.append(class_def)

    return class_name


def _generate_policy_document_wrapper_block(
    doc: dict[str, Any],
    parent_logical_id: str,
    property_path: str,
    ctx: "CodegenContext",
) -> str:
    """
    Generate a @cloudformation_dataclass wrapper for a PolicyDocument.

    Returns the generated class name.
    """
    # Generate class name
    # Convert property_path to PascalCase for class name suffix
    path_suffix = "".join(word.title() for word in property_path.replace(".", "_").split("_"))
    class_name = f"{parent_logical_id}{path_suffix}"

    # Handle name collisions
    if class_name in ctx.generated_classes:
        i = 1
        while f"{class_name}{i}" in ctx.generated_classes:
            i += 1
        class_name = f"{class_name}{i}"

    ctx.generated_classes.add(class_name)

    # Add imports
    ctx.add_import("cloudformation_dataclasses.core", "PolicyDocument")
    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    lines = []
    lines.append("    resource: PolicyDocument")

    # Handle version if not default
    # Note: YAML may parse "2012-10-17" as a datetime.date, so convert to string
    version = doc.get("Version", "2012-10-17")
    if isinstance(version, (datetime.date, datetime.datetime)):
        version = version.strftime("%Y-%m-%d")
    if version != "2012-10-17":
        lines.append(f"    version = {escape_string(version)}")

    # Generate wrapper classes for each statement
    statements = doc.get("Statement", [])
    if statements:
        stmt_class_names = []
        for i, stmt in enumerate(statements):
            if isinstance(stmt, dict):
                stmt_class = _generate_policy_statement_wrapper_block(
                    stmt, parent_logical_id, f"{property_path}.statement.{i}",
                    i, ctx
                )
                stmt_class_names.append(stmt_class)
            else:
                # Handle non-dict statements (unlikely but possible)
                stmt_class_names.append(repr(stmt))

        if len(stmt_class_names) == 1:
            lines.append(f"    statement = [{stmt_class_names[0]}]")
        else:
            lines.append(f"    statement = [{', '.join(stmt_class_names)}]")

    # Store class definition
    class_def = f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)
    ctx.property_type_class_defs.append(class_def)

    return class_name


# =============================================================================
# Condition to Python
# =============================================================================


def condition_to_python(
    condition: dict[str, Any], ctx: "CodegenContext", indent: int = 0
) -> str:
    """Convert a policy condition dict to Python code with operator constants.

    Transforms: {"Bool": {"key": "value"}} -> {BOOL: {"key": "value"}}
    """
    indent_str = "    " * indent

    if not condition:
        return "{}"

    items = []
    for operator, conditions in condition.items():
        # Use constant if available, otherwise string
        if operator in CONDITION_OPERATOR_MAP:
            const_name = CONDITION_OPERATOR_MAP[operator]
            ctx.add_condition_operator_import(const_name)
            key_str = const_name
        else:
            key_str = escape_string(operator)

        val_str = value_to_python(conditions, ctx, indent + 1)
        items.append(f"{key_str}: {val_str}")

    inner = f",\n{indent_str}    ".join(items)
    return f"{{\n{indent_str}    {inner},\n{indent_str}}}"
