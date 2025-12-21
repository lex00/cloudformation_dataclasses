"""Python code generation from IR."""

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Literal, Optional

from cloudformation_dataclasses.constants import (
    CONDITION_OPERATOR_MAP,
    PARAMETER_TYPE_MAP,
    PSEUDO_PARAMETER_MAP,
    find_property_type_for_cf_keys,
    get_property_type_info,
    resolve_resource_type,
)
from cloudformation_dataclasses.importer.ir import (
    IntrinsicType,
    IRCondition,
    IRIntrinsic,
    IRMapping,
    IROutput,
    IRParameter,
    IRResource,
    IRTemplate,
)
from cloudformation_dataclasses.importer.parser import to_snake_case


class OutputMode(Enum):
    """Code generation output modes."""

    BLOCK = "block"  # Maximize declarative wrapper classes
    BRIEF = "brief"  # Maximize imperative, direct instantiation
    MIXED = "mixed"  # Balanced approach


# =============================================================================
# Code Generation Context
# =============================================================================


@dataclass
class CodegenContext:
    """Context for code generation."""

    template: IRTemplate
    mode: OutputMode = OutputMode.BLOCK
    include_docstrings: bool = True
    include_main_block: bool = True

    # Tracking during generation
    generated_classes: set[str] = field(default_factory=set)
    imports: dict[str, set[str]] = field(default_factory=dict)  # module -> class names
    intrinsic_imports: set[str] = field(default_factory=set)

    # For mixed mode: track reuse counts
    tag_reuse: dict[str, int] = field(default_factory=dict)  # "Key:Value" -> count

    # Current module being generated (for PropertyType resolution)
    current_module: Optional[str] = None

    # For block mode: collect PropertyType wrapper class definitions
    # These are generated during resource class generation and inserted before resources
    property_type_class_defs: list[str] = field(default_factory=list)

    def add_import(self, module: str, name: str) -> None:
        """Add an import to track."""
        self.imports.setdefault(module, set()).add(name)

    def add_intrinsic_import(self, name: str) -> None:
        """Add an intrinsic function import."""
        self.intrinsic_imports.add(name)

    def add_condition_operator_import(self, const_name: str) -> None:
        """Add a condition operator constant import."""
        if const_name.startswith("ConditionOperator."):
            self.add_import("cloudformation_dataclasses.core", "ConditionOperator")
        else:
            # It's an alias like STRING_EQUALS, BOOL, etc.
            self.add_import("cloudformation_dataclasses.core", const_name)

    def add_parameter_type_import(self, const_name: str) -> None:
        """Add a parameter type constant import."""
        if const_name.startswith("ParameterType."):
            self.add_import("cloudformation_dataclasses.core", "ParameterType")
        else:
            # It's an alias like STRING, NUMBER
            self.add_import("cloudformation_dataclasses.core", const_name)


def _analyze_reuse(template: IRTemplate) -> dict[str, int]:
    """Analyze tag reuse for mixed mode decisions."""
    tag_counts: dict[str, int] = {}

    for resource in template.resources.values():
        if "Tags" in resource.properties:
            tags_prop = resource.properties["Tags"]
            if isinstance(tags_prop.value, list):
                for tag in tags_prop.value:
                    if isinstance(tag, dict):
                        key = tag.get("Key", "")
                        value = tag.get("Value", "")
                        sig = f"{key}:{value}"
                        tag_counts[sig] = tag_counts.get(sig, 0) + 1

    return tag_counts


def _tag_class_name(key: str, value: str) -> str:
    """Generate a class name for a tag."""

    # Convert key and value to PascalCase
    def to_pascal(s: str) -> str:
        return "".join(word.title() for word in re.sub(r"[^a-zA-Z0-9]", " ", s).split())

    return f"{to_pascal(key)}{to_pascal(value)}Tag"


def _tag_signature(tag: dict[str, Any]) -> str:
    """Get the signature for a tag (Key:Value)."""
    return f"{tag.get('Key', '')}:{tag.get('Value', '')}"


# =============================================================================
# Value Serialization
# =============================================================================

# Known enum mappings: (module, enum_class) -> {string_value: constant_name}
# Used during code generation to convert string literals to enum references
KNOWN_ENUMS: dict[tuple[str, str], dict[str, str]] = {
    # S3 enums
    ("s3", "ServerSideEncryption"): {
        "AES256": "AES256",
        "aws:kms": "AWS_KMS",
        "aws:kms:dsse": "AWS_KMS_DSSE",
    },
    ("s3", "BucketVersioningStatus"): {
        "Enabled": "ENABLED",
        "Suspended": "SUSPENDED",
    },
    ("s3", "ObjectLockEnabled"): {
        "Enabled": "ENABLED",
    },
    ("s3", "ObjectLockMode"): {
        "COMPLIANCE": "COMPLIANCE",
        "GOVERNANCE": "GOVERNANCE",
    },
    ("s3", "ObjectLockRetentionMode"): {
        "COMPLIANCE": "COMPLIANCE",
        "GOVERNANCE": "GOVERNANCE",
    },
    ("s3", "ReplicationRuleStatus"): {
        "Enabled": "ENABLED",
        "Disabled": "DISABLED",
    },
    # DynamoDB enums
    ("dynamodb", "KeyType"): {
        "HASH": "HASH",
        "RANGE": "RANGE",
    },
    ("dynamodb", "AttributeType"): {
        "S": "S",
        "N": "N",
        "B": "B",
    },
    ("dynamodb", "BillingMode"): {
        "PROVISIONED": "PROVISIONED",
        "PAY_PER_REQUEST": "PAY_PER_REQUEST",
    },
    ("dynamodb", "ProjectionType"): {
        "ALL": "ALL",
        "KEYS_ONLY": "KEYS_ONLY",
        "INCLUDE": "INCLUDE",
    },
    ("dynamodb", "StreamViewType"): {
        "KEYS_ONLY": "KEYS_ONLY",
        "NEW_IMAGE": "NEW_IMAGE",
        "OLD_IMAGE": "OLD_IMAGE",
        "NEW_AND_OLD_IMAGES": "NEW_AND_OLD_IMAGES",
    },
    # Lambda enums
    ("lambda_", "Runtime"): {
        "python3.8": "PYTHON3_8",
        "python3.9": "PYTHON3_9",
        "python3.10": "PYTHON3_10",
        "python3.11": "PYTHON3_11",
        "python3.12": "PYTHON3_12",
        "python3.13": "PYTHON3_13",
        "nodejs18.x": "NODEJS18_X",
        "nodejs20.x": "NODEJS20_X",
        "nodejs22.x": "NODEJS22_X",
    },
}


# Known type wrapper names to skip when extracting class names
_SKIP_TYPE_NAMES = frozenset({
    "Optional", "Union", "Any", "Ref", "GetAtt", "Sub", "ClassVar",
    "List", "Dict", "Set", "Tuple", "Callable", "Sequence", "Mapping",
    "list", "dict", "set", "tuple", "bool", "str", "int", "float",
})


def _extract_class_from_type_hint(type_hint: Optional[str]) -> Optional[str]:
    """
    Extract a PropertyType class name from a type annotation string.

    Args:
        type_hint: Type annotation like "Optional[BucketEncryption]" or
                   "Optional[list[ServerSideEncryptionRule]]"

    Returns:
        Class name (e.g., "BucketEncryption") or None if no class found.
    """
    if not type_hint:
        return None

    # Find all PascalCase identifiers in the type hint
    for match in re.finditer(r"\b([A-Z][a-zA-Z0-9]*)\b", type_hint):
        class_name = match.group(1)
        if class_name not in _SKIP_TYPE_NAMES:
            return class_name

    return None


def _extract_enum_from_type_hint(type_hint: str) -> Optional[tuple[str, str]]:
    """
    Extract enum class name from a type annotation string.

    Args:
        type_hint: Type annotation like "Optional[Union[str, ServerSideEncryption, Ref, ...]]"

    Returns:
        Tuple of (module, enum_class) if found, None otherwise.
    """
    # Look for known enum class names in the type hint
    for (module, enum_class), _ in KNOWN_ENUMS.items():
        if enum_class in type_hint:
            return (module, enum_class)
    return None


def _try_convert_to_enum(
    value: str, type_hint: Optional[str], ctx: CodegenContext
) -> Optional[str]:
    """
    Try to convert a string value to an enum constant reference.

    Args:
        value: The string value to convert
        type_hint: Type annotation string (if known)
        ctx: Code generation context

    Returns:
        Enum reference string (e.g., "ServerSideEncryption.AES256") or None
    """
    if not type_hint:
        return None

    enum_info = _extract_enum_from_type_hint(type_hint)
    if not enum_info:
        return None

    module, enum_class = enum_info
    enum_values = KNOWN_ENUMS.get((module, enum_class))
    if not enum_values or value not in enum_values:
        return None

    const_name = enum_values[value]
    # Add import
    full_module = f"cloudformation_dataclasses.aws.{module}"
    ctx.add_import(full_module, enum_class)
    return f"{enum_class}.{const_name}"


def _value_to_python_typed(
    value: Any,
    ctx: CodegenContext,
    indent: int = 0,
    expected_type: Optional[str] = None,
    expected_module: Optional[str] = None,
    expected_class: Optional[str] = None,
) -> str:
    """
    Convert a value to Python source code, using PropertyType classes when possible.

    Args:
        value: The value to convert
        ctx: Code generation context
        indent: Current indentation level
        expected_type: Type annotation string (for enum detection)
        expected_module: Expected module for PropertyType (e.g., "s3")
        expected_class: Expected PropertyType class name (e.g., "BucketEncryption")

    Returns:
        Python source code string
    """
    indent_str = "    " * indent

    if isinstance(value, IRIntrinsic):
        return _intrinsic_to_python(value, ctx)

    if value is None:
        return "None"

    if isinstance(value, bool):
        return "True" if value else "False"

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        # Try enum conversion if we have type information
        if expected_type:
            enum_ref = _try_convert_to_enum(value, expected_type, ctx)
            if enum_ref:
                return enum_ref
        return _escape_string(value)

    if isinstance(value, list):
        if not value:
            return "[]"

        # Check if this is a list of PropertyTypes
        inner_type = None
        inner_module = None
        inner_class = None
        if expected_type:
            # Extract inner type from list[...] annotation
            list_match = re.match(r".*list\[(\w+)\].*", expected_type, re.IGNORECASE)
            if list_match:
                inner_class = list_match.group(1)
                # Try to find this PropertyType
                if expected_module:
                    info = get_property_type_info(expected_module, inner_class)
                    if info:
                        inner_module = expected_module

        items = []
        for item in value:
            item_str = _value_to_python_typed(
                item, ctx, indent + 1,
                expected_type=inner_type,
                expected_module=inner_module,
                expected_class=inner_class,
            )
            items.append(item_str)

        if len(items) == 1:
            return f"[{items[0]}]"
        inner = f",\n{indent_str}    ".join(items)
        return f"[\n{indent_str}    {inner},\n{indent_str}]"

    if isinstance(value, dict):
        if not value:
            return "{}"

        # Try to match to a PropertyType
        cf_keys = set(value.keys())
        module_hint = expected_module or ctx.current_module

        # If we have an expected class, check if it matches
        property_type_info = None
        pt_module = None
        pt_class = None

        if expected_class and expected_module:
            property_type_info = get_property_type_info(expected_module, expected_class)
            if property_type_info:
                pt_module = expected_module
                pt_class = expected_class
        else:
            # Try to find a matching PropertyType
            match = find_property_type_for_cf_keys(cf_keys, module_hint=module_hint)
            if match:
                pt_module, pt_class = match
                property_type_info = get_property_type_info(pt_module, pt_class)

        if property_type_info and pt_module and pt_class:
            # Convert to PropertyType constructor
            cf_to_python = property_type_info["cf_to_python"]
            field_types = property_type_info["field_types"]

            # Build constructor arguments
            args = []
            for cf_key, val in value.items():
                if cf_key in cf_to_python:
                    python_field = cf_to_python[cf_key]
                    field_type = field_types.get(python_field)

                    # Check if field type references another PropertyType
                    nested_module = None
                    nested_class = _extract_class_from_type_hint(field_type)
                    if nested_class:
                        nested_module = pt_module

                    val_str = _value_to_python_typed(
                        val, ctx, indent + 1,
                        expected_type=field_type,
                        expected_module=nested_module,
                        expected_class=nested_class,
                    )
                    args.append(f"{python_field}={val_str}")
                else:
                    # Unknown key - still include it but as-is
                    val_str = _value_to_python_typed(val, ctx, indent + 1)
                    args.append(f"# Unknown: {cf_key}={val_str}")

            # Add import for PropertyType
            full_module = f"cloudformation_dataclasses.aws.{pt_module}"
            ctx.add_import(full_module, pt_class)

            if len(args) == 1:
                return f"{pt_class}({args[0]})"
            inner = f",\n{indent_str}    ".join(args)
            return f"{pt_class}(\n{indent_str}    {inner},\n{indent_str})"

        # No PropertyType match - fall back to dict
        items = []
        for k, v in value.items():
            key_str = _escape_string(k) if isinstance(k, str) else str(k)
            val_str = _value_to_python_typed(v, ctx, indent + 1)
            items.append(f"{key_str}: {val_str}")
        inner = f",\n{indent_str}    ".join(items)
        return f"{{\n{indent_str}    {inner},\n{indent_str}}}"

    return repr(value)


def _escape_string(s: str) -> str:
    """Escape a string for Python source code."""
    # Use repr for proper escaping, but handle multi-line strings
    if "\n" in s:
        # Use triple quotes for multi-line
        escaped = s.replace('"""', '\\"\\"\\"')
        return f'"""{escaped}"""'
    return repr(s)


def _value_to_python(value: Any, ctx: CodegenContext, indent: int = 0) -> str:
    """Convert a value to Python source code."""
    indent_str = "    " * indent

    if isinstance(value, IRIntrinsic):
        return _intrinsic_to_python(value, ctx)

    if value is None:
        return "None"

    if isinstance(value, bool):
        return "True" if value else "False"

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        return _escape_string(value)

    if isinstance(value, list):
        if not value:
            return "[]"
        if len(value) == 1:
            return f"[{_value_to_python(value[0], ctx, indent)}]"
        items = [_value_to_python(item, ctx, indent + 1) for item in value]
        inner = f",\n{indent_str}    ".join(items)
        return f"[\n{indent_str}    {inner},\n{indent_str}]"

    if isinstance(value, dict):
        if not value:
            return "{}"
        items = []
        for k, v in value.items():
            key_str = _escape_string(k) if isinstance(k, str) else str(k)
            val_str = _value_to_python(v, ctx, indent + 1)
            items.append(f"{key_str}: {val_str}")
        inner = f",\n{indent_str}    ".join(items)
        return f"{{\n{indent_str}    {inner},\n{indent_str}}}"

    return repr(value)


def _intrinsic_to_python(intrinsic: IRIntrinsic, ctx: CodegenContext) -> str:
    """Convert an IRIntrinsic to Python code."""
    if intrinsic.type == IntrinsicType.REF:
        target = intrinsic.args
        # Check if it's a parameter, resource, or pseudo-parameter
        if target.startswith("AWS::"):
            # Pseudo-parameter - use constant if available
            if target in PSEUDO_PARAMETER_MAP:
                const_name = PSEUDO_PARAMETER_MAP[target]
                ctx.add_intrinsic_import(const_name)
                return const_name
            # Unknown pseudo-parameter
            ctx.add_intrinsic_import("Ref")
            return f'Ref("{target}")'
        if target in ctx.template.parameters:
            return f"ref({target})"
        if target in ctx.template.resources:
            return f"ref({target})"
        # Unknown reference - use string
        ctx.add_intrinsic_import("Ref")
        return f'Ref("{target}")'

    if intrinsic.type == IntrinsicType.GET_ATT:
        logical_id, attr = intrinsic.args
        if logical_id in ctx.template.resources:
            return f'get_att({logical_id}, "{attr}")'
        ctx.add_intrinsic_import("GetAtt")
        return f'GetAtt("{logical_id}", "{attr}")'

    if intrinsic.type == IntrinsicType.SUB:
        ctx.add_intrinsic_import("Sub")
        if isinstance(intrinsic.args, str):
            return f"Sub({_escape_string(intrinsic.args)})"
        template_str, variables = intrinsic.args
        if variables:
            vars_str = _value_to_python(variables, ctx)
            return f"Sub({_escape_string(template_str)}, {vars_str})"
        return f"Sub({_escape_string(template_str)})"

    if intrinsic.type == IntrinsicType.JOIN:
        ctx.add_intrinsic_import("Join")
        delimiter, values = intrinsic.args
        values_str = _value_to_python(values, ctx)
        return f"Join({_escape_string(delimiter)}, {values_str})"

    if intrinsic.type == IntrinsicType.SELECT:
        ctx.add_intrinsic_import("Select")
        index, list_val = intrinsic.args
        list_str = _value_to_python(list_val, ctx)
        return f"Select({index}, {list_str})"

    if intrinsic.type == IntrinsicType.GET_AZS:
        ctx.add_intrinsic_import("GetAZs")
        region = intrinsic.args
        if region:
            return f"GetAZs({_escape_string(region)})"
        return "GetAZs()"

    if intrinsic.type == IntrinsicType.IF:
        ctx.add_intrinsic_import("If")
        cond_name, true_val, false_val = intrinsic.args
        true_str = _value_to_python(true_val, ctx)
        false_str = _value_to_python(false_val, ctx)
        return f'If("{cond_name}", {true_str}, {false_str})'

    if intrinsic.type == IntrinsicType.EQUALS:
        ctx.add_intrinsic_import("Equals")
        val1, val2 = intrinsic.args
        str1 = _value_to_python(val1, ctx)
        str2 = _value_to_python(val2, ctx)
        return f"Equals({str1}, {str2})"

    if intrinsic.type == IntrinsicType.AND:
        ctx.add_intrinsic_import("And")
        conditions = [_value_to_python(c, ctx) for c in intrinsic.args]
        return f"And({', '.join(conditions)})"

    if intrinsic.type == IntrinsicType.OR:
        ctx.add_intrinsic_import("Or")
        conditions = [_value_to_python(c, ctx) for c in intrinsic.args]
        return f"Or({', '.join(conditions)})"

    if intrinsic.type == IntrinsicType.NOT:
        ctx.add_intrinsic_import("Not")
        cond_str = _value_to_python(intrinsic.args, ctx)
        return f"Not({cond_str})"

    if intrinsic.type == IntrinsicType.CONDITION:
        ctx.add_intrinsic_import("Condition")
        return f'Condition("{intrinsic.args}")'

    if intrinsic.type == IntrinsicType.FIND_IN_MAP:
        ctx.add_intrinsic_import("FindInMap")
        map_name, top_key, second_key = intrinsic.args
        top_str = _value_to_python(top_key, ctx)
        second_str = _value_to_python(second_key, ctx)
        return f'FindInMap("{map_name}", {top_str}, {second_str})'

    if intrinsic.type == IntrinsicType.BASE64:
        ctx.add_intrinsic_import("Base64")
        val_str = _value_to_python(intrinsic.args, ctx)
        return f"Base64({val_str})"

    if intrinsic.type == IntrinsicType.CIDR:
        ctx.add_intrinsic_import("Cidr")
        ip_block, count, cidr_bits = intrinsic.args
        block_str = _value_to_python(ip_block, ctx)
        return f"Cidr({block_str}, {count}, {cidr_bits})"

    if intrinsic.type == IntrinsicType.IMPORT_VALUE:
        ctx.add_intrinsic_import("ImportValue")
        val_str = _value_to_python(intrinsic.args, ctx)
        return f"ImportValue({val_str})"

    if intrinsic.type == IntrinsicType.SPLIT:
        ctx.add_intrinsic_import("Split")
        delimiter, source = intrinsic.args
        source_str = _value_to_python(source, ctx)
        return f"Split({_escape_string(delimiter)}, {source_str})"

    if intrinsic.type == IntrinsicType.TRANSFORM:
        ctx.add_intrinsic_import("Transform")
        val_str = _value_to_python(intrinsic.args, ctx)
        return f"Transform({val_str})"

    # Fallback
    return f"# Unknown intrinsic: {intrinsic.type}"


# =============================================================================
# Block Mode PropertyType Wrapper Generation
# =============================================================================


def _property_value_to_python_block(
    value: Any,
    parent_logical_id: str,
    property_path: str,
    expected_type: Optional[str],
    expected_module: Optional[str],
    ctx: CodegenContext,
) -> str:
    """
    Convert a property value to Python code in block mode.

    For PropertyTypes: generates separate wrapper class, returns class name.
    For primitives/enums: returns literal value.
    For lists of PropertyTypes: returns [WrapperClassName].
    """
    if isinstance(value, IRIntrinsic):
        return _intrinsic_to_python(value, ctx)

    if value is None:
        return "None"

    if isinstance(value, bool):
        return "True" if value else "False"

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        # Try enum conversion
        if expected_type:
            enum_ref = _try_convert_to_enum(value, expected_type, ctx)
            if enum_ref:
                return enum_ref
        return _escape_string(value)

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
            item_str = _property_value_to_python_block(
                item,
                parent_logical_id,
                f"{property_path}.{i}",
                f"Optional[{inner_class}]" if inner_class else expected_type,
                expected_module,
                ctx,
            )
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
        expected_class = _extract_class_from_type_hint(expected_type)

        if expected_class and expected_module:
            pt_info = get_property_type_info(expected_module, expected_class)
            if pt_info:
                # Generate wrapper class, return class name
                class_name = _generate_property_type_wrapper(
                    value,
                    parent_logical_id,
                    property_path,
                    expected_module,
                    expected_class,
                    ctx,
                )
                return class_name

        # Try to find matching PropertyType by keys
        cf_keys = set(value.keys())
        match = find_property_type_for_cf_keys(cf_keys, module_hint=expected_module)
        if match:
            pt_module, pt_class = match
            class_name = _generate_property_type_wrapper(
                value,
                parent_logical_id,
                property_path,
                pt_module,
                pt_class,
                ctx,
            )
            return class_name

        # Fall back to dict literal
        return _value_to_python(value, ctx, indent=1)

    return repr(value)


def _generate_property_type_wrapper(
    value: dict[str, Any],
    parent_logical_id: str,
    property_path: str,
    pt_module: str,
    pt_class: str,
    ctx: CodegenContext,
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
        return _value_to_python(value, ctx, indent=1)

    cf_to_python = property_type_info["cf_to_python"]
    field_types = property_type_info["field_types"]

    lines = []
    lines.append(f"    resource: {pt_class}")

    # Add import for PropertyType
    ctx.add_import(f"cloudformation_dataclasses.aws.{pt_module}", pt_class)

    # Convert each field
    for cf_key, val in value.items():
        if cf_key in cf_to_python:
            python_field = cf_to_python[cf_key]
            field_type = field_types.get(python_field)

            # Recursively handle nested PropertyTypes
            val_str = _property_value_to_python_block(
                val,
                parent_logical_id,
                f"{property_path}.{python_field}",
                field_type,
                pt_module,
                ctx,
            )
            lines.append(f"    {python_field} = {val_str}")
        else:
            # Unknown key - still include it but as comment
            val_str = _value_to_python(val, ctx, indent=1)
            lines.append(f"    # Unknown CF key: {cf_key} = {val_str}")

    # Add import for decorator
    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    # Store class definition
    class_def = f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)
    ctx.property_type_class_defs.append(class_def)

    return class_name


def _generate_policy_statement_wrapper_block(
    stmt: dict[str, Any],
    parent_logical_id: str,
    property_path: str,
    stmt_index: int,
    ctx: CodegenContext,
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
    # Note: We use _value_to_python here (not _property_value_to_python_block)
    # because principal/action/resource are plain values, not PropertyTypes
    if "Sid" in stmt:
        lines.append(f"    sid = {_escape_string(stmt['Sid'])}")

    if "Principal" in stmt:
        principal_str = _value_to_python(stmt["Principal"], ctx, indent=1)
        lines.append(f"    principal = {principal_str}")

    if "Action" in stmt:
        action_str = _value_to_python(stmt["Action"], ctx, indent=1)
        lines.append(f"    action = {action_str}")

    if "Resource" in stmt:
        resource_str = _value_to_python(stmt["Resource"], ctx, indent=1)
        lines.append(f"    resource_arn = {resource_str}")

    if "Condition" in stmt:
        condition_str = _condition_to_python(stmt["Condition"], ctx, indent=1)
        lines.append(f"    condition = {condition_str}")

    # Store class definition
    class_def = f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)
    ctx.property_type_class_defs.append(class_def)

    return class_name


def _generate_policy_document_wrapper_block(
    doc: dict[str, Any],
    parent_logical_id: str,
    property_path: str,
    ctx: CodegenContext,
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
    version = doc.get("Version", "2012-10-17")
    if version != "2012-10-17":
        lines.append(f"    version = {_escape_string(version)}")

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
# Block Mode Class Generation
# =============================================================================


def _generate_parameter_class(param: IRParameter, ctx: CodegenContext) -> str:
    """Generate a parameter wrapper class."""
    lines = []

    # Docstring
    if ctx.include_docstrings and param.description:
        lines.append(f'    """{param.description}"""')
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
        lines.append(f"    type = {_escape_string(param.type)}")

    # Optional fields
    if param.description:
        lines.append(f"    description = {_escape_string(param.description)}")
    if param.default is not None:
        lines.append(f"    default = {_value_to_python(param.default, ctx)}")
    if param.allowed_values:
        lines.append(f"    allowed_values = {_value_to_python(param.allowed_values, ctx)}")
    if param.allowed_pattern:
        lines.append(f"    allowed_pattern = {_escape_string(param.allowed_pattern)}")
    if param.min_length is not None:
        lines.append(f"    min_length = {param.min_length}")
    if param.max_length is not None:
        lines.append(f"    max_length = {param.max_length}")
    if param.min_value is not None:
        lines.append(f"    min_value = {param.min_value}")
    if param.max_value is not None:
        lines.append(f"    max_value = {param.max_value}")
    if param.constraint_description:
        lines.append(f"    constraint_description = {_escape_string(param.constraint_description)}")
    if param.no_echo:
        lines.append("    no_echo = True")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {param.logical_id}:\n" + "\n".join(lines)


def _generate_resource_class(resource: IRResource, ctx: CodegenContext) -> str:
    """Generate a resource wrapper class."""
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
        ctx.add_import(f"cloudformation_dataclasses.aws.{module}", class_name)
        lines.append(f"    resource: {class_name}")

        # Get field type information for this resource class
        # We need to scan the resource class for _property_mappings and field types
        try:
            import cloudformation_dataclasses.aws as aws_pkg
            from pathlib import Path
            aws_dir = Path(aws_pkg.__file__).parent
            py_file = aws_dir / f"{module}.py"
            if py_file.exists():
                content = py_file.read_text()
                # Find the resource class and its field types
                in_target_class = False
                brace_depth = 0
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

        value_str = _property_value_to_python_block(
            prop.value,
            resource.logical_id,
            prop.python_name,
            expected_type,
            resource_module,
            ctx,
        )
        lines.append(f"    {prop.python_name} = {value_str}")

    # Resource-level attributes
    if resource.depends_on:
        deps = ", ".join(resource.depends_on)
        lines.append(f"    depends_on = [{deps}]")
    if resource.condition:
        lines.append(f"    condition = {_escape_string(resource.condition)}")
    if resource.deletion_policy:
        lines.append(f"    deletion_policy = {_escape_string(resource.deletion_policy)}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {resource.logical_id}:\n" + "\n".join(lines)


def _generate_output_class(output: IROutput, ctx: CodegenContext) -> str:
    """Generate an output wrapper class."""
    lines = []

    # Docstring
    if ctx.include_docstrings and output.description:
        lines.append(f'    """{output.description}"""')
        lines.append("")

    ctx.add_import("cloudformation_dataclasses.core", "Output")
    lines.append("    resource: Output")

    # Value
    value_str = _value_to_python(output.value, ctx, indent=1)
    lines.append(f"    value = {value_str}")

    # Optional fields
    if output.description:
        lines.append(f"    description = {_escape_string(output.description)}")
    if output.export_name:
        export_str = _value_to_python(output.export_name, ctx, indent=1)
        lines.append(f"    export_name = {export_str}")
    if output.condition:
        lines.append(f"    condition = {_escape_string(output.condition)}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {output.logical_id}Output:\n" + "\n".join(lines)


def _generate_mapping_class(mapping: IRMapping, ctx: CodegenContext) -> str:
    """Generate a mapping wrapper class."""
    lines = []

    ctx.add_import("cloudformation_dataclasses.core", "Mapping")
    lines.append("    resource: Mapping")

    # Map data as dict
    map_str = _value_to_python(mapping.map_data, ctx, indent=1)
    lines.append(f"    map_data = {map_str}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {mapping.logical_id}Mapping:\n" + "\n".join(lines)


def _generate_condition_class(condition: IRCondition, ctx: CodegenContext) -> str:
    """Generate a condition wrapper class."""
    lines = []

    ctx.add_import("cloudformation_dataclasses.core", "Condition")
    lines.append("    resource: Condition")

    # Expression
    expr_str = _value_to_python(condition.expression, ctx, indent=1)
    lines.append(f"    expression = {expr_str}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {condition.logical_id}Condition:\n" + "\n".join(lines)


def _generate_tag_class(key: str, value: str, ctx: CodegenContext) -> str:
    """Generate a tag wrapper class for mixed mode."""
    lines = []
    class_name = _tag_class_name(key, value)

    ctx.add_import("cloudformation_dataclasses.core", "Tag")
    lines.append("    resource: Tag")
    lines.append(f"    key = {_escape_string(key)}")
    lines.append(f"    value = {_escape_string(value)}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)


def _tag_to_python_mixed(tag: dict[str, Any], ctx: CodegenContext) -> str:
    """Convert a tag to Python code in mixed mode.

    If the tag is reused (appears 2+ times), reference the class.
    Otherwise, inline it.
    """
    key = tag.get("Key", "")
    value = tag.get("Value", "")
    sig = _tag_signature(tag)

    if ctx.tag_reuse.get(sig, 0) >= 2:
        # Reference the tag class
        return _tag_class_name(key, value)
    else:
        # Inline the tag
        ctx.add_import("cloudformation_dataclasses.core", "Tag")
        return f"Tag(key={_escape_string(key)}, value={_escape_string(value)})"


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


def _condition_to_python(
    condition: dict[str, Any], ctx: CodegenContext, indent: int = 0
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
            key_str = _escape_string(operator)

        val_str = _value_to_python_mixed(conditions, ctx, indent + 1)
        items.append(f"{key_str}: {val_str}")

    inner = f",\n{indent_str}    ".join(items)
    return f"{{\n{indent_str}    {inner},\n{indent_str}}}"


def _statement_to_python_mixed(stmt: dict[str, Any], ctx: CodegenContext, indent: int = 0) -> str:
    """Convert a policy statement dict to PolicyStatement code."""
    indent_str = "    " * indent
    inner_indent = "    " * (indent + 1)

    ctx.add_import("cloudformation_dataclasses.core", "PolicyStatement")

    args = []

    if "Sid" in stmt:
        args.append(f"sid={_escape_string(stmt['Sid'])}")

    effect = stmt.get("Effect", "Allow")
    if effect != "Allow":
        args.append(f"effect={_escape_string(effect)}")

    if "Principal" in stmt:
        principal = stmt["Principal"]
        principal_str = _value_to_python_mixed(principal, ctx, indent + 1)
        args.append(f"principal={principal_str}")

    if "Action" in stmt:
        action = stmt["Action"]
        action_str = _value_to_python_mixed(action, ctx, indent + 1)
        args.append(f"action={action_str}")

    if "Resource" in stmt:
        resource = stmt["Resource"]
        resource_str = _value_to_python_mixed(resource, ctx, indent + 1)
        args.append(f"resource_arn={resource_str}")

    if "Condition" in stmt:
        condition = stmt["Condition"]
        condition_str = _condition_to_python(condition, ctx, indent + 1)
        args.append(f"condition={condition_str}")

    if len(args) <= 2:
        return f"PolicyStatement({', '.join(args)})"
    else:
        args_str = f",\n{inner_indent}".join(args)
        return f"PolicyStatement(\n{inner_indent}{args_str},\n{indent_str})"


def _policy_document_to_python_mixed(
    doc: dict[str, Any], ctx: CodegenContext, indent: int = 0
) -> str:
    """Convert a policy document dict to PolicyDocument code."""
    inner_indent = "    " * (indent + 1)

    ctx.add_import("cloudformation_dataclasses.core", "PolicyDocument")

    version = doc.get("Version", "2012-10-17")
    statements = doc.get("Statement", [])

    # Convert statements
    stmt_strs = [_statement_to_python_mixed(s, ctx, indent + 2) for s in statements]

    if len(stmt_strs) == 1:
        stmt_list = f"[{stmt_strs[0]}]"
    else:
        stmt_inner = f",\n{inner_indent}    ".join(stmt_strs)
        stmt_list = f"[\n{inner_indent}    {stmt_inner},\n{inner_indent}]"

    if version == "2012-10-17":
        return f"PolicyDocument(statement={stmt_list})"
    else:
        return f"PolicyDocument(version={_escape_string(version)}, statement={stmt_list})"


def _value_to_python_mixed(value: Any, ctx: CodegenContext, indent: int = 0) -> str:
    """Convert a value to Python source code in mixed mode.

    Special handling for:
    - Tags: inline or reference based on reuse
    - Policy documents: use PolicyDocument/PolicyStatement classes
    """
    indent_str = "    " * indent

    if isinstance(value, IRIntrinsic):
        return _intrinsic_to_python(value, ctx)

    if value is None:
        return "None"

    if isinstance(value, bool):
        return "True" if value else "False"

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        return _escape_string(value)

    if isinstance(value, list):
        if not value:
            return "[]"
        # Check if this looks like a Tags list
        if value and isinstance(value[0], dict) and "Key" in value[0] and "Value" in value[0]:
            items = [_tag_to_python_mixed(tag, ctx) for tag in value]
            if len(items) == 1:
                return f"[{items[0]}]"
            inner = f",\n{indent_str}    ".join(items)
            return f"[\n{indent_str}    {inner},\n{indent_str}]"
        # Regular list
        if len(value) == 1:
            return f"[{_value_to_python_mixed(value[0], ctx, indent)}]"
        items = [_value_to_python_mixed(item, ctx, indent + 1) for item in value]
        inner = f",\n{indent_str}    ".join(items)
        return f"[\n{indent_str}    {inner},\n{indent_str}]"

    if isinstance(value, dict):
        if not value:
            return "{}"

        # Check if this is a policy document
        if _is_policy_document(value):
            return _policy_document_to_python_mixed(value, ctx, indent)

        # Regular dict
        items = []
        for k, v in value.items():
            key_str = _escape_string(k) if isinstance(k, str) else str(k)
            val_str = _value_to_python_mixed(v, ctx, indent + 1)
            items.append(f"{key_str}: {val_str}")
        inner = f",\n{indent_str}    ".join(items)
        return f"{{\n{indent_str}    {inner},\n{indent_str}}}"

    return repr(value)


def _generate_resource_class_mixed(resource: IRResource, ctx: CodegenContext) -> str:
    """Generate a resource wrapper class in mixed mode.

    Uses _value_to_python_mixed for tag inlining support.
    """
    lines = []

    # Docstring
    if ctx.include_docstrings:
        lines.append(f'    """{resource.resource_type} resource."""')
        lines.append("")

    # Resolve resource type
    resolved = resolve_resource_type(resource.resource_type)
    if resolved:
        module, class_name = resolved
        ctx.add_import(f"cloudformation_dataclasses.aws.{module}", class_name)
        lines.append(f"    resource: {class_name}")
    else:
        # Unknown resource type - use comment
        lines.append(f"    # Unknown resource type: {resource.resource_type}")
        lines.append("    resource: CloudFormationResource")
        ctx.add_import("cloudformation_dataclasses.core", "CloudFormationResource")

    # Properties - use mixed mode value conversion
    for prop in resource.properties.values():
        value_str = _value_to_python_mixed(prop.value, ctx, indent=1)
        lines.append(f"    {prop.python_name} = {value_str}")

    # Resource-level attributes
    if resource.depends_on:
        deps = ", ".join(resource.depends_on)
        lines.append(f"    depends_on = [{deps}]")
    if resource.condition:
        lines.append(f"    condition = {_escape_string(resource.condition)}")
    if resource.deletion_policy:
        lines.append(f"    deletion_policy = {_escape_string(resource.deletion_policy)}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {resource.logical_id}:\n" + "\n".join(lines)


def _generate_template_class(template: IRTemplate, ctx: CodegenContext) -> tuple[str, str]:
    """Generate template build info (description and parameters list).

    Resources are auto-registered via @cloudformation_dataclass, so we use
    Template.from_registry() instead of generating a template wrapper class.
    """
    # Determine template name from source file
    if template.source_file and template.source_file not in ("<string>", "<stream>"):
        # Extract name from path
        name = re.sub(
            r"[^a-zA-Z0-9]", "_", template.source_file.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        )
        name = "".join(word.title() for word in name.split("_"))
        template_name = f"{name}Template"
    else:
        template_name = "GeneratedTemplate"

    return "", template_name


# =============================================================================
# Brief Mode Generation (Imperative)
# =============================================================================


def _generate_parameter_imperative(param: IRParameter, ctx: CodegenContext) -> str:
    """Generate a parameter as an imperative instantiation."""
    ctx.add_import("cloudformation_dataclasses.core", "Parameter")

    args = [f'logical_id="{param.logical_id}"']
    # Type - use constant if available
    if param.type in PARAMETER_TYPE_MAP:
        const_name = PARAMETER_TYPE_MAP[param.type]
        ctx.add_parameter_type_import(const_name)
        args.append(f"type={const_name}")
    else:
        args.append(f"type={_escape_string(param.type)}")

    if param.description:
        args.append(f"description={_escape_string(param.description)}")
    if param.default is not None:
        args.append(f"default={_value_to_python(param.default, ctx)}")
    if param.allowed_values:
        args.append(f"allowed_values={_value_to_python(param.allowed_values, ctx)}")
    if param.allowed_pattern:
        args.append(f"allowed_pattern={_escape_string(param.allowed_pattern)}")
    if param.min_length is not None:
        args.append(f"min_length={param.min_length}")
    if param.max_length is not None:
        args.append(f"max_length={param.max_length}")
    if param.min_value is not None:
        args.append(f"min_value={param.min_value}")
    if param.max_value is not None:
        args.append(f"max_value={param.max_value}")
    if param.constraint_description:
        args.append(f"constraint_description={_escape_string(param.constraint_description)}")
    if param.no_echo:
        args.append("no_echo=True")

    var_name = to_snake_case(param.logical_id)
    if len(args) <= 3:
        return f"{var_name} = Parameter({', '.join(args)})"
    else:
        args_str = ",\n    ".join(args)
        return f"{var_name} = Parameter(\n    {args_str},\n)"


def _generate_resource_imperative(resource: IRResource, ctx: CodegenContext) -> str:
    """Generate a resource as an imperative instantiation."""
    resolved = resolve_resource_type(resource.resource_type)
    if resolved:
        module, class_name = resolved
        ctx.add_import(f"cloudformation_dataclasses.aws.{module}", class_name)
    else:
        class_name = "CloudFormationResource"
        ctx.add_import("cloudformation_dataclasses.core", "CloudFormationResource")

    args = [f'logical_id="{resource.logical_id}"']

    # Properties
    for prop in resource.properties.values():
        value_str = _value_to_python(prop.value, ctx)
        args.append(f"{prop.python_name}={value_str}")

    # Resource-level attributes
    if resource.depends_on:
        deps = ", ".join(f'"{d}"' for d in resource.depends_on)
        args.append(f"depends_on=[{deps}]")
    if resource.condition:
        args.append(f"condition={_escape_string(resource.condition)}")
    if resource.deletion_policy:
        args.append(f"deletion_policy={_escape_string(resource.deletion_policy)}")

    var_name = to_snake_case(resource.logical_id)
    if len(args) <= 2:
        return f"{var_name} = {class_name}({', '.join(args)})"
    else:
        args_str = ",\n    ".join(args)
        return f"{var_name} = {class_name}(\n    {args_str},\n)"


def _generate_output_imperative(output: IROutput, ctx: CodegenContext) -> str:
    """Generate an output as an imperative instantiation."""
    ctx.add_import("cloudformation_dataclasses.core", "Output")

    args = [f'logical_id="{output.logical_id}"']
    args.append(f"value={_value_to_python(output.value, ctx)}")

    if output.description:
        args.append(f"description={_escape_string(output.description)}")
    if output.export_name:
        args.append(f"export_name={_value_to_python(output.export_name, ctx)}")
    if output.condition:
        args.append(f"condition={_escape_string(output.condition)}")

    var_name = to_snake_case(output.logical_id) + "_output"
    if len(args) <= 3:
        return f"{var_name} = Output({', '.join(args)})"
    else:
        args_str = ",\n    ".join(args)
        return f"{var_name} = Output(\n    {args_str},\n)"


def _generate_template_imperative(template: IRTemplate, ctx: CodegenContext) -> str:
    """Generate the template as an imperative instantiation."""
    ctx.add_import("cloudformation_dataclasses.core", "Template")

    args = []
    if template.description:
        args.append(f"description={_escape_string(template.description)}")

    # Parameters
    if template.parameters:
        param_vars = ", ".join(to_snake_case(lid) for lid in template.parameters.keys())
        args.append(f"parameters=[{param_vars}]")

    # Resources
    if template.resources:
        resource_vars = ", ".join(to_snake_case(lid) for lid in template.resources.keys())
        args.append(f"resources=[{resource_vars}]")

    # Outputs
    if template.outputs:
        output_vars = ", ".join(to_snake_case(lid) + "_output" for lid in template.outputs.keys())
        args.append(f"outputs=[{output_vars}]")

    if len(args) <= 2:
        return f"template = Template({', '.join(args)})"
    else:
        args_str = ",\n    ".join(args)
        return f"template = Template(\n    {args_str},\n)"


# =============================================================================
# Import Generation
# =============================================================================


def _generate_imports(ctx: CodegenContext) -> str:
    """Generate import statements."""
    lines = []

    # Group imports by package
    core_imports = ctx.imports.get("cloudformation_dataclasses.core", set())
    if core_imports:
        sorted_imports = sorted(core_imports)
        if len(sorted_imports) <= 3:
            lines.append(f"from cloudformation_dataclasses.core import {', '.join(sorted_imports)}")
        else:
            lines.append("from cloudformation_dataclasses.core import (")
            for name in sorted_imports:
                lines.append(f"    {name},")
            lines.append(")")

    # AWS module imports
    aws_modules = sorted(
        (mod, names)
        for mod, names in ctx.imports.items()
        if mod.startswith("cloudformation_dataclasses.aws.")
    )
    for module, names in aws_modules:
        sorted_names = sorted(names)
        if len(sorted_names) <= 3:
            lines.append(f"from {module} import {', '.join(sorted_names)}")
        else:
            lines.append(f"from {module} import (")
            for name in sorted_names:
                lines.append(f"    {name},")
            lines.append(")")

    # Intrinsic imports
    if ctx.intrinsic_imports:
        sorted_intrinsics = sorted(ctx.intrinsic_imports)
        if len(sorted_intrinsics) <= 3:
            lines.append(
                f"from cloudformation_dataclasses.intrinsics import {', '.join(sorted_intrinsics)}"
            )
        else:
            lines.append("from cloudformation_dataclasses.intrinsics import (")
            for name in sorted_intrinsics:
                lines.append(f"    {name},")
            lines.append(")")

    return "\n".join(lines)


# =============================================================================
# Topological Sort
# =============================================================================


def _topological_sort(template: IRTemplate) -> list[str]:
    """Sort resources so dependencies come first."""
    visited: set[str] = set()
    result: list[str] = []

    def visit(resource_id: str) -> None:
        if resource_id in visited:
            return
        visited.add(resource_id)

        # Visit dependencies first
        for dep_id in template.reference_graph.get(resource_id, []):
            if dep_id in template.resources:
                visit(dep_id)

        result.append(resource_id)

    for resource_id in template.resources:
        visit(resource_id)

    return result


# =============================================================================
# Main Code Generation
# =============================================================================


def generate_code(
    template: IRTemplate,
    mode: Literal["block", "brief", "mixed"] = "block",
    include_main: bool = True,
    lint: bool = True,
) -> str:
    """
    Generate Python code from analyzed IR.

    Args:
        template: Parsed IRTemplate
        mode: Output mode - "block" (declarative), "brief" (imperative), or "mixed"
        include_main: Include if __name__ == "__main__" block
        lint: Run linter on generated code to apply fixes (default: True).
              This catches any string literals that should use type-safe constants.

    Returns:
        Complete Python module source code
    """
    output_mode = OutputMode(mode)
    ctx = CodegenContext(
        template=template,
        mode=output_mode,
        include_main_block=include_main,
    )

    # Analyze reuse for mixed mode
    if output_mode == OutputMode.MIXED:
        ctx.tag_reuse = _analyze_reuse(template)

    # Add ref and get_att imports (commonly needed)
    ctx.add_import("cloudformation_dataclasses.core", "ref")
    ctx.add_import("cloudformation_dataclasses.core", "get_att")

    sections: list[str] = []

    # Module docstring
    if template.description:
        sections.append(f'"""\n{template.description}\n\nGenerated by cfn-import.\n"""')
    else:
        sections.append('"""Generated by cfn-import."""')

    if output_mode == OutputMode.BRIEF:
        code = _generate_brief_mode(template, ctx, sections, include_main)
    elif output_mode == OutputMode.MIXED:
        code = _generate_mixed_mode(template, ctx, sections, include_main)
    else:
        code = _generate_block_mode(template, ctx, sections, include_main)

    # Optionally run linter to fix any remaining issues
    if lint:
        from cloudformation_dataclasses.linter import fix_code

        code = fix_code(code, add_imports=True)

    return code


def _generate_block_mode(
    template: IRTemplate,
    ctx: CodegenContext,
    sections: list[str],
    include_main: bool,
) -> str:
    """Generate block mode (declarative) code."""
    class_sections: list[str] = []

    # Parameters
    for param in template.parameters.values():
        class_sections.append(_generate_parameter_class(param, ctx))

    # Mappings
    for mapping in template.mappings.values():
        class_sections.append(_generate_mapping_class(mapping, ctx))

    # Conditions
    for condition in template.conditions.values():
        class_sections.append(_generate_condition_class(condition, ctx))

    # Resources (in dependency order)
    # For each resource, first insert any PropertyType wrappers generated for it,
    # then the resource class itself. This ensures proper ordering since
    # PropertyType wrappers may use ref() to reference other resources.
    sorted_resources = _topological_sort(template)
    for resource_id in sorted_resources:
        resource = template.resources[resource_id]
        # Clear PropertyType class defs before generating this resource
        ctx.property_type_class_defs = []
        resource_class = _generate_resource_class(resource, ctx)
        # Add PropertyType wrappers for this resource (generated during resource class generation)
        class_sections.extend(ctx.property_type_class_defs)
        # Then add the resource class itself
        class_sections.append(resource_class)

    # Outputs
    for output in template.outputs.values():
        class_sections.append(_generate_output_class(output, ctx))

    # No template wrapper class - resources auto-register via @cloudformation_dataclass
    # Use Template.from_registry() in build_template()

    # Now generate imports
    ctx.add_import("cloudformation_dataclasses.core", "Template")
    sections.append(_generate_imports(ctx))

    # Add class sections (filter out empty strings)
    sections.extend(s for s in class_sections if s)

    # Build template function using Template.from_registry()
    # Build parameter list if any
    param_list = ""
    if template.parameters:
        param_names = ", ".join(template.parameters.keys())
        param_list = f"parameters=[{param_names}]"

    # Build output list if any
    output_list = ""
    if template.outputs:
        output_names = ", ".join(f"{lid}Output" for lid in template.outputs.keys())
        output_list = f"outputs=[{output_names}]"

    # Build the from_registry call
    args = []
    if template.description:
        args.append(f"description={_escape_string(template.description)}")
    if param_list:
        args.append(param_list)
    if output_list:
        args.append(output_list)

    if args:
        args_str = ",\n        ".join(args)
        from_registry_call = f"Template.from_registry(\n        {args_str},\n    )"
    else:
        from_registry_call = "Template.from_registry()"

    sections.append(
        f"""
def build_template() -> Template:
    \"\"\"Build the CloudFormation template.\"\"\"
    return {from_registry_call}"""
    )

    # Main block
    if include_main:
        sections.append(
            """
if __name__ == "__main__":
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))"""
        )

    return "\n\n\n".join(sections) + "\n"


# =============================================================================
# Package Generation (Multi-file Output)
# =============================================================================


@dataclass
class PackageContext:
    """Context for package generation - tracks imports per file."""

    template: IRTemplate
    mode: OutputMode = OutputMode.BLOCK

    # Per-file imports
    init_imports: dict[str, set[str]] = field(default_factory=dict)
    config_classes: list[str] = field(default_factory=list)
    resources_classes: list[str] = field(default_factory=list)
    main_classes: list[str] = field(default_factory=list)

    # Cross-file references (for explicit imports)
    # Maps: file -> set of class names from other files it references
    config_exports: set[str] = field(default_factory=set)
    resources_exports: set[str] = field(default_factory=set)

    # For generating classes, we need a CodegenContext
    codegen_ctx: CodegenContext = field(default=None)

    def __post_init__(self):
        if self.codegen_ctx is None:
            self.codegen_ctx = CodegenContext(
                template=self.template,
                mode=self.mode,
            )


def _generate_init_py(pkg_ctx: PackageContext, template: IRTemplate) -> str:
    """Generate __init__.py with centralized imports."""
    lines = []

    # Docstring from template description
    if template.description:
        # Truncate long descriptions
        desc = template.description.strip()
        if len(desc) > 200:
            desc = desc[:197] + "..."
        lines.append(f'"""{desc}\n\nGenerated by cfn-import."""')
    else:
        lines.append('"""Generated by cfn-import."""')

    lines.append("")

    # Generate import statements from collected imports
    ctx = pkg_ctx.codegen_ctx

    # Core imports
    core_imports = ctx.imports.get("cloudformation_dataclasses.core", set())
    # Always include these
    core_imports.add("cloudformation_dataclass")
    core_imports.add("ref")
    core_imports.add("get_att")
    core_imports.add("Template")

    if core_imports:
        sorted_imports = sorted(core_imports)
        if len(sorted_imports) <= 4:
            lines.append(
                f"from cloudformation_dataclasses.core import {', '.join(sorted_imports)}"
            )
        else:
            lines.append("from cloudformation_dataclasses.core import (")
            for name in sorted_imports:
                lines.append(f"    {name},")
            lines.append(")")

    # AWS module imports
    aws_modules = sorted(
        (mod, names)
        for mod, names in ctx.imports.items()
        if mod.startswith("cloudformation_dataclasses.aws.")
    )
    for module, names in aws_modules:
        sorted_names = sorted(names)
        if len(sorted_names) <= 4:
            lines.append(f"from {module} import {', '.join(sorted_names)}")
        else:
            lines.append(f"from {module} import (")
            for name in sorted_names:
                lines.append(f"    {name},")
            lines.append(")")

    # Intrinsic imports
    if ctx.intrinsic_imports:
        sorted_intrinsics = sorted(ctx.intrinsic_imports)
        if len(sorted_intrinsics) <= 4:
            lines.append(
                f"from cloudformation_dataclasses.intrinsics import "
                f"{', '.join(sorted_intrinsics)}"
            )
        else:
            lines.append("from cloudformation_dataclasses.intrinsics import (")
            for name in sorted_intrinsics:
                lines.append(f"    {name},")
            lines.append(")")

    lines.append("")

    # Generate __all__ with all exported names
    all_names = sorted(core_imports | set().union(*[names for _, names in aws_modules]))
    if ctx.intrinsic_imports:
        all_names = sorted(set(all_names) | ctx.intrinsic_imports)

    lines.append("__all__ = [")
    for name in all_names:
        lines.append(f'    "{name}",')
    lines.append("]")

    return "\n".join(lines) + "\n"


def _generate_config_py(pkg_ctx: PackageContext, template: IRTemplate) -> str:
    """Generate config.py with Parameters, Mappings, Conditions."""
    lines = []
    lines.append('"""Configuration - Parameters, Mappings, Conditions."""')
    lines.append("")
    lines.append("from . import *  # noqa: F403")
    lines.append("")
    lines.append("")

    ctx = pkg_ctx.codegen_ctx

    # Parameters
    for param in template.parameters.values():
        class_def = _generate_parameter_class(param, ctx)
        lines.append(class_def)
        lines.append("")
        lines.append("")
        pkg_ctx.config_exports.add(param.logical_id)

    # Mappings
    for mapping in template.mappings.values():
        class_def = _generate_mapping_class(mapping, ctx)
        lines.append(class_def)
        lines.append("")
        lines.append("")
        pkg_ctx.config_exports.add(f"{mapping.logical_id}Mapping")

    # Conditions
    for condition in template.conditions.values():
        class_def = _generate_condition_class(condition, ctx)
        lines.append(class_def)
        lines.append("")
        lines.append("")
        pkg_ctx.config_exports.add(f"{condition.logical_id}Condition")

    # Remove trailing empty lines
    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines) + "\n"


def _generate_resources_py(pkg_ctx: PackageContext, template: IRTemplate) -> str:
    """Generate resources.py with Resources and PropertyType wrappers."""
    lines = []
    lines.append('"""Resource definitions."""')
    lines.append("")
    lines.append("from . import *  # noqa: F403")

    ctx = pkg_ctx.codegen_ctx

    # Add explicit imports for config classes referenced by resources
    # (for ref() calls to parameters)
    config_refs = _find_config_references(template)
    if config_refs:
        sorted_refs = sorted(config_refs)
        lines.append(f"from .config import {', '.join(sorted_refs)}")

    lines.append("")
    lines.append("")

    # Resources (in dependency order)
    sorted_resources = _topological_sort(template)
    for resource_id in sorted_resources:
        resource = template.resources[resource_id]
        # Clear PropertyType class defs before generating this resource
        ctx.property_type_class_defs = []
        resource_class = _generate_resource_class(resource, ctx)
        # Add PropertyType wrappers for this resource
        for pt_class in ctx.property_type_class_defs:
            lines.append(pt_class)
            lines.append("")
            lines.append("")
        # Then add the resource class itself
        lines.append(resource_class)
        lines.append("")
        lines.append("")
        pkg_ctx.resources_exports.add(resource.logical_id)

    # Remove trailing empty lines
    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines) + "\n"


def _generate_main_py(pkg_ctx: PackageContext, template: IRTemplate) -> str:
    """Generate main.py with Outputs, build_template, and __main__."""
    lines = []
    lines.append('"""Template outputs and builder."""')
    lines.append("")
    lines.append("from . import *  # noqa: F403")

    ctx = pkg_ctx.codegen_ctx

    # Add explicit imports from config (for parameters in build_template)
    if pkg_ctx.config_exports:
        sorted_exports = sorted(pkg_ctx.config_exports)
        lines.append(f"from .config import {', '.join(sorted_exports)}")

    # Add explicit imports from resources (for ref/get_att in outputs)
    resource_refs = _find_resource_references_in_outputs(template)
    if resource_refs:
        sorted_refs = sorted(resource_refs)
        lines.append(f"from .resources import {', '.join(sorted_refs)}")

    lines.append("")
    lines.append("")

    # Outputs
    for output in template.outputs.values():
        class_def = _generate_output_class(output, ctx)
        lines.append(class_def)
        lines.append("")
        lines.append("")

    # Build template function
    param_list = ""
    if template.parameters:
        param_names = ", ".join(template.parameters.keys())
        param_list = f"parameters=[{param_names}]"

    output_list = ""
    if template.outputs:
        output_names = ", ".join(f"{lid}Output" for lid in template.outputs.keys())
        output_list = f"outputs=[{output_names}]"

    args = []
    if template.description:
        args.append(f"description={_escape_string(template.description)}")
    if param_list:
        args.append(param_list)
    if output_list:
        args.append(output_list)

    if args:
        args_str = ",\n        ".join(args)
        from_registry_call = f"Template.from_registry(\n        {args_str},\n    )"
    else:
        from_registry_call = "Template.from_registry()"

    lines.append("def build_template() -> Template:")
    lines.append('    """Build the CloudFormation template."""')
    lines.append(f"    return {from_registry_call}")
    lines.append("")
    lines.append("")

    # Main block
    lines.append('if __name__ == "__main__":')
    lines.append("    import json")
    lines.append("    template = build_template()")
    lines.append("    print(json.dumps(template.to_dict(), indent=2))")

    return "\n".join(lines) + "\n"


def _find_config_references(template: IRTemplate) -> set[str]:
    """Find parameter/mapping/condition names referenced by resources."""
    refs = set()
    for resource in template.resources.values():
        # Check for references in the reference graph
        for ref_target in template.reference_graph.get(resource.logical_id, []):
            if ref_target in template.parameters:
                refs.add(ref_target)
            elif ref_target in template.mappings:
                refs.add(f"{ref_target}Mapping")
            elif ref_target in template.conditions:
                refs.add(f"{ref_target}Condition")
    return refs


def _find_resource_references_in_outputs(template: IRTemplate) -> set[str]:
    """Find resource names referenced by outputs (for get_att/ref)."""
    refs = set()
    for output in template.outputs.values():
        # Check reference graph for this output
        for ref_target in template.reference_graph.get(output.logical_id, []):
            if ref_target in template.resources:
                refs.add(ref_target)
    return refs


def generate_package(
    template: IRTemplate,
    mode: Literal["block", "brief", "mixed"] = "block",
    lint: bool = True,
) -> dict[str, str]:
    """
    Generate a Python package from template (multi-file output).

    Args:
        template: Parsed IRTemplate
        mode: Output mode - "block" (declarative), "brief" (imperative), or "mixed"
        lint: Run linter on generated code (default: True)

    Returns:
        Dict mapping filename to content:
        - "__init__.py": Centralized imports
        - "config.py": Parameters, Mappings, Conditions
        - "resources.py": Resources and PropertyType wrappers
        - "main.py": Outputs + build_template
    """
    output_mode = OutputMode(mode)
    pkg_ctx = PackageContext(template=template, mode=output_mode)

    # Initialize codegen context
    ctx = pkg_ctx.codegen_ctx
    ctx.add_import("cloudformation_dataclasses.core", "ref")
    ctx.add_import("cloudformation_dataclasses.core", "get_att")
    ctx.add_import("cloudformation_dataclasses.core", "Template")

    # Analyze tag reuse for mixed mode
    if output_mode == OutputMode.MIXED:
        ctx.tag_reuse = _analyze_reuse(template)

    # Generate files in order (to collect imports)
    config_content = _generate_config_py(pkg_ctx, template)
    resources_content = _generate_resources_py(pkg_ctx, template)
    main_content = _generate_main_py(pkg_ctx, template)

    # Generate __init__.py last (after all imports collected)
    init_content = _generate_init_py(pkg_ctx, template)

    files = {
        "__init__.py": init_content,
        "config.py": config_content,
        "resources.py": resources_content,
        "main.py": main_content,
    }

    # Optionally run linter on each file
    if lint:
        from cloudformation_dataclasses.linter import fix_code

        for filename, content in files.items():
            files[filename] = fix_code(content, add_imports=True)

    return files


def _generate_brief_mode(
    template: IRTemplate,
    ctx: CodegenContext,
    sections: list[str],
    include_main: bool,
) -> str:
    """Generate brief mode (imperative) code."""
    code_sections: list[str] = []

    # Parameters
    for param in template.parameters.values():
        code_sections.append(_generate_parameter_imperative(param, ctx))

    # Resources (in dependency order)
    sorted_resources = _topological_sort(template)
    for resource_id in sorted_resources:
        resource = template.resources[resource_id]
        code_sections.append(_generate_resource_imperative(resource, ctx))

    # Outputs
    for output in template.outputs.values():
        code_sections.append(_generate_output_imperative(output, ctx))

    # Template
    code_sections.append(_generate_template_imperative(template, ctx))

    # Now generate imports
    sections.append(_generate_imports(ctx))

    # Add code sections
    sections.extend(code_sections)

    # Main block
    if include_main:
        sections.append(
            """
if __name__ == "__main__":
    import json
    print(json.dumps(template.to_dict(), indent=2))"""
        )

    return "\n\n\n".join(sections) + "\n"


def _generate_mixed_mode(
    template: IRTemplate,
    ctx: CodegenContext,
    sections: list[str],
    include_main: bool,
) -> str:
    """Generate mixed mode code.

    Mixed mode rules:
    - Resources, parameters, outputs: always wrapper classes
    - Tags: inline if used once, wrapper class if reused (2+ times)
    - Nested property types: inline if ≤3 fields, wrapper if >3 (future)
    """
    class_sections: list[str] = []

    # Parameters (always classes)
    for param in template.parameters.values():
        class_sections.append(_generate_parameter_class(param, ctx))

    # Mappings (always classes)
    for mapping in template.mappings.values():
        class_sections.append(_generate_mapping_class(mapping, ctx))

    # Conditions (always classes)
    for condition in template.conditions.values():
        class_sections.append(_generate_condition_class(condition, ctx))

    # Generate tag classes for reused tags (before resources that reference them)
    generated_tags: set[str] = set()
    for sig, count in ctx.tag_reuse.items():
        if count >= 2 and sig not in generated_tags:
            key, value = sig.split(":", 1)
            class_sections.append(_generate_tag_class(key, value, ctx))
            generated_tags.add(sig)

    # Resources (always classes, in dependency order, using mixed mode)
    sorted_resources = _topological_sort(template)
    for resource_id in sorted_resources:
        resource = template.resources[resource_id]
        class_sections.append(_generate_resource_class_mixed(resource, ctx))

    # Outputs (always classes)
    for output in template.outputs.values():
        class_sections.append(_generate_output_class(output, ctx))

    # No template wrapper class - resources auto-register via @cloudformation_dataclass
    # Use Template.from_registry() in build_template()

    # Now generate imports
    ctx.add_import("cloudformation_dataclasses.core", "Template")
    sections.append(_generate_imports(ctx))

    # Add class sections (filter out empty strings)
    sections.extend(s for s in class_sections if s)

    # Build template function using Template.from_registry()
    # Build parameter list if any
    param_list = ""
    if template.parameters:
        param_names = ", ".join(template.parameters.keys())
        param_list = f"parameters=[{param_names}]"

    # Build output list if any
    output_list = ""
    if template.outputs:
        output_names = ", ".join(f"{lid}Output" for lid in template.outputs.keys())
        output_list = f"outputs=[{output_names}]"

    # Build the from_registry call
    args = []
    if template.description:
        args.append(f"description={_escape_string(template.description)}")
    if param_list:
        args.append(param_list)
    if output_list:
        args.append(output_list)

    if args:
        args_str = ",\n        ".join(args)
        from_registry_call = f"Template.from_registry(\n        {args_str},\n    )"
    else:
        from_registry_call = "Template.from_registry()"

    sections.append(
        f"""
def build_template() -> Template:
    \"\"\"Build the CloudFormation template.\"\"\"
    return {from_registry_call}"""
    )

    # Main block
    if include_main:
        sections.append(
            """
if __name__ == "__main__":
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))"""
        )

    return "\n\n\n".join(sections) + "\n"
