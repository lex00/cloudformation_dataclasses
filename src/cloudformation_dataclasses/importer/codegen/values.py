"""Value serialization to Python source code."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, Optional

from cloudformation_dataclasses.constants import (
    PSEUDO_PARAMETER_MAP,
    find_property_type_for_cf_keys,
    get_property_type_info,
)
from cloudformation_dataclasses.importer.ir import (
    IntrinsicType,
    IRIntrinsic,
)

from .context import AnnotatedValue
from .helpers import (
    KNOWN_ENUMS,
    extract_class_from_type_hint,
    extract_enum_from_type_hint,
    resolve_property_type,
)

if TYPE_CHECKING:
    from .context import CodegenContext


# =============================================================================
# String Escaping
# =============================================================================


def escape_string(s: str) -> str:
    """Escape a string for Python source code."""
    # Use repr for proper escaping, but handle multi-line strings
    if "\n" in s:
        # Use triple quotes for multi-line
        if '"""' not in s:
            return f'"""{s}"""'
        # Contains triple double quotes - try triple single quotes
        if "'''" not in s:
            return f"'''{s}'''"
        # Both quote styles present - fall back to repr
        return repr(s)
    return repr(s)


def escape_docstring(s: str) -> str:
    """Escape a string for use as a docstring.

    Returns the docstring with proper quoting to avoid syntax errors.
    """
    # If contains triple double quotes, escape them
    if '"""' in s:
        escaped = s.replace('"""', '\\"\\"\\"')
        return f'"""{escaped}"""'
    # If contains double quotes that would break the docstring, use repr-style escaping
    if '"' in s and s.endswith('"'):
        # Ending with " followed by """ breaks syntax
        escaped = s.replace('"', '\\"')
        return f'"""{escaped}"""'
    return f'"""{s}"""'


# =============================================================================
# Enum Conversion
# =============================================================================


def try_convert_to_enum(
    value: str, type_hint: Optional[str], ctx: "CodegenContext"
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

    enum_info = extract_enum_from_type_hint(type_hint)
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


# =============================================================================
# AnnotatedValue Conversion
# =============================================================================


def annotated_to_class_ref(annotated: AnnotatedValue) -> str:
    """Convert an AnnotatedValue to a class-based ref for inline use.

    AnnotatedValue is for top-level properties only. When used inline
    (in lists, dicts, etc.), we use class-based refs like ref(ClassName).
    """
    # Extract target from annotation like "Ref[Bucket]" -> "Bucket"
    if match := re.match(r"Ref\[(\w+)\]", annotated.annotation):
        target = match.group(1)
        return f"ref({target})"
    elif match := re.match(r"GetAtt\[(\w+)\]", annotated.annotation):
        target = match.group(1)
        # Extract attribute from value like 'get_att("Arn")' -> "Arn"
        if attr_match := re.search(r'get_att\("(\w+)"\)', annotated.value):
            attr = attr_match.group(1)
            return f'get_att({target}, "{attr}")'
        # Handle get_att(ARN) constant - extract constant name
        if "(" in annotated.value:
            const = annotated.value.split("(")[1].rstrip(")")
            return f"get_att({target}, {const})"
        return f"get_att({target})"
    # Fallback - shouldn't happen
    return annotated.value


# =============================================================================
# Value to Python (Simple)
# =============================================================================


def value_to_python(
    value: Any,
    ctx: "CodegenContext",
    indent: int = 0,
    parent_property_type: tuple[str, str] | None = None,
    use_property_type_keys: bool = True,
) -> str:
    """Convert a value to Python source code.

    Args:
        value: The value to convert
        ctx: Code generation context
        indent: Current indentation level
        parent_property_type: Optional (module, class_name) of parent PropertyType for dict key constants
        use_property_type_keys: If False, don't use PropertyType constants for dict keys (for Mapping data)
    """
    from cloudformation_dataclasses.importer.parser import to_snake_case

    indent_str = "    " * indent

    if isinstance(value, IRIntrinsic):
        result = intrinsic_to_python(value, ctx)
        # AnnotatedValue is only for top-level properties, not inline values
        if isinstance(result, AnnotatedValue):
            return annotated_to_class_ref(result)
        return result

    if value is None:
        return "None"

    if isinstance(value, bool):
        return "True" if value else "False"

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        return escape_string(value)

    if isinstance(value, list):
        if not value:
            return "[]"
        if len(value) == 1:
            return f"[{value_to_python(value[0], ctx, indent, parent_property_type, use_property_type_keys)}]"
        items = [value_to_python(item, ctx, indent + 1, parent_property_type, use_property_type_keys) for item in value]
        inner = f",\n{indent_str}    ".join(items)
        return f"[\n{indent_str}    {inner},\n{indent_str}]"

    if isinstance(value, dict):
        if not value:
            return "{}"

        # Try to find the PropertyType for this dict based on its keys
        # Skip for Mapping data (use_property_type_keys=False)
        cf_keys = set(value.keys())
        module_hint = parent_property_type[0] if parent_property_type else ctx.current_module
        dict_property_type = None
        if use_property_type_keys:
            dict_property_type = find_property_type_for_cf_keys(cf_keys, module_hint)

        items = []
        for k, v in value.items():
            # Generate dict key - use PropertyType constant if available
            if dict_property_type:
                module, class_name = dict_property_type
                const_name = to_snake_case(k)  # PropertyType attrs are lowercase snake_case
                key_str = f"{class_name}.{const_name}"
                ctx.add_import(f"cloudformation_dataclasses.aws.{module}", class_name)
            else:
                key_str = escape_string(k) if isinstance(k, str) else str(k)

            # For nested dicts, determine the child PropertyType from the key name
            child_property_type = None
            if isinstance(v, (dict, list)) and module_hint:
                child_info = get_property_type_info(module_hint, k)
                if child_info:
                    child_property_type = (module_hint, k)

            val_str = value_to_python(v, ctx, indent + 1, child_property_type, use_property_type_keys)
            items.append(f"{key_str}: {val_str}")
        inner = f",\n{indent_str}    ".join(items)
        return f"{{\n{indent_str}    {inner},\n{indent_str}}}"

    return repr(value)


# =============================================================================
# Value to Python (Typed - with PropertyType conversion)
# =============================================================================


def value_to_python_typed(
    value: Any,
    ctx: "CodegenContext",
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
        result = intrinsic_to_python(value, ctx)
        # AnnotatedValue is only for top-level properties, not inline values
        if isinstance(result, AnnotatedValue):
            return annotated_to_class_ref(result)
        return result

    if value is None:
        return "None"

    if isinstance(value, bool):
        return "True" if value else "False"

    if isinstance(value, (int, float)):
        return str(value)

    if isinstance(value, str):
        # Try enum conversion if we have type information
        if expected_type:
            enum_ref = try_convert_to_enum(value, expected_type, ctx)
            if enum_ref:
                return enum_ref
        return escape_string(value)

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
            item_str = value_to_python_typed(
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

        resolved = resolve_property_type(
            expected_class, expected_module, cf_keys, module_hint
        )

        if resolved:
            pt_module, pt_class, property_type_info = resolved
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
                    nested_class = extract_class_from_type_hint(field_type)
                    if nested_class:
                        nested_module = pt_module

                    val_str = value_to_python_typed(
                        val, ctx, indent + 1,
                        expected_type=field_type,
                        expected_module=nested_module,
                        expected_class=nested_class,
                    )
                    args.append(f"{python_field}={val_str}")
                else:
                    # Unknown key - still include it but as-is
                    val_str = value_to_python_typed(val, ctx, indent + 1)
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
            key_str = escape_string(k) if isinstance(k, str) else str(k)
            val_str = value_to_python_typed(v, ctx, indent + 1)
            items.append(f"{key_str}: {val_str}")
        inner = f",\n{indent_str}    ".join(items)
        return f"{{\n{indent_str}    {inner},\n{indent_str}}}"

    return repr(value)


# =============================================================================
# Intrinsic to Python
# =============================================================================


def intrinsic_to_python(intrinsic: IRIntrinsic, ctx: "CodegenContext") -> str | AnnotatedValue:
    """Convert an IRIntrinsic to Python code."""

    def _format_ref_target(logical_id: str) -> str:
        """Format a ref/get_att target - use PascalCase class names."""
        return logical_id

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
            # Class ref for parameters - they're defined in stack_config.py and re-exported
            return f"ref({_format_ref_target(target)})"
        if target in ctx.template.resources:
            # Check if this is a forward reference (defined later in same SCC file)
            if target in ctx.forward_references:
                # Use string-based ref to avoid NameError at class definition time
                return f'ref("{_format_ref_target(target)}")'
            # Class-based ref for resources
            return f"ref({_format_ref_target(target)})"
        # Unknown reference - use string
        ctx.add_intrinsic_import("Ref")
        return f'Ref("{target}")'

    if intrinsic.type == IntrinsicType.GET_ATT:
        logical_id, attr = intrinsic.args
        if logical_id in ctx.template.resources:
            # Check if this is a forward reference (defined later in same SCC file)
            if logical_id in ctx.forward_references:
                # Use string-based get_att to avoid NameError at class definition time
                return f'get_att("{_format_ref_target(logical_id)}", "{attr}")'
            # Class-based get_att for resources
            return f'get_att({_format_ref_target(logical_id)}, "{attr}")'
        ctx.add_intrinsic_import("GetAtt")
        return f'GetAtt("{logical_id}", "{attr}")'

    if intrinsic.type == IntrinsicType.SUB:
        # Extract template string for pattern matching
        if isinstance(intrinsic.args, str):
            template_str = intrinsic.args
            variables = None
        else:
            template_str, variables = intrinsic.args

        # Check if this Sub pattern builds an ARN matching a resource's ARN
        # If so, use get_att(Resource, "Arn") for proper dependency tracking
        if not variables and template_str in ctx.arn_pattern_map:
            resource_id, suffix = ctx.arn_pattern_map[template_str]
            # Don't replace if this is the same resource
            if resource_id != ctx.current_resource_id:
                # Check if the Sub references only parameters (not resource-derived values)
                # If so, don't replace with get_att - keep the original Sub expression
                var_refs = re.findall(r"\$\{([^}]+)\}", template_str)
                # Filter out pseudo-parameters (AWS::*)
                non_pseudo_vars = [v for v in var_refs if not v.startswith("AWS::")]
                # If all non-pseudo vars are parameters, skip get_att replacement
                all_params = all(v in ctx.template.parameters for v in non_pseudo_vars)
                if not all_params:
                    ctx.add_import("cloudformation_dataclasses.core", "ARN")
                    ctx.add_import("cloudformation_dataclasses.core", "GetAtt")
                    formatted_id = _format_ref_target(resource_id)
                    if suffix == "":
                        # Exact ARN match - annotation-based ref
                        return AnnotatedValue(
                            annotation=f"GetAtt[{formatted_id}]", value="get_att(ARN)"
                        )
                    else:
                        # ARN with suffix (e.g., "/*") - use Join for simple concatenation
                        # This case is complex, keep as string ref for now
                        ctx.add_intrinsic_import("Join")
                        return f"Join('', [get_att(\"{formatted_id}\", ARN), '{suffix}'])"

        # Check if this Sub pattern matches a resource's name property
        # If so, use ref() for proper dependency tracking
        # But skip if this is the same resource (avoid self-referential ref)
        if not variables and template_str in ctx.name_pattern_map:
            resource_id = ctx.name_pattern_map[template_str]
            # Don't replace if this is the resource that defines this name pattern
            if resource_id != ctx.current_resource_id:
                # Check if this is a forward reference (defined later in same SCC file)
                if resource_id in ctx.forward_references:
                    # Use string-based ref to avoid NameError at class definition time
                    return f'ref("{_format_ref_target(resource_id)}")'
                # Class-based ref for resource
                return f"ref({_format_ref_target(resource_id)})"

        # Fall back to Sub() intrinsic
        ctx.add_intrinsic_import("Sub")
        if variables:
            vars_str = value_to_python(variables, ctx)
            return f"Sub({escape_string(template_str)}, {vars_str})"
        return f"Sub({escape_string(template_str)})"

    if intrinsic.type == IntrinsicType.JOIN:
        ctx.add_intrinsic_import("Join")
        delimiter, values = intrinsic.args
        values_str = value_to_python(values, ctx)
        return f"Join({escape_string(delimiter)}, {values_str})"

    if intrinsic.type == IntrinsicType.SELECT:
        ctx.add_intrinsic_import("Select")
        index, list_val = intrinsic.args
        list_str = value_to_python(list_val, ctx)
        return f"Select({index}, {list_str})"

    if intrinsic.type == IntrinsicType.GET_AZS:
        ctx.add_intrinsic_import("GetAZs")
        region = intrinsic.args
        if region:
            # Region can be a string or an intrinsic like !Ref AWS::Region
            if isinstance(region, IRIntrinsic):
                region_str = intrinsic_to_python(region, ctx)
                return f"GetAZs({region_str})"
            return f"GetAZs({escape_string(region)})"
        return "GetAZs()"

    if intrinsic.type == IntrinsicType.IF:
        ctx.add_intrinsic_import("If")
        cond_name, true_val, false_val = intrinsic.args
        true_str = value_to_python(true_val, ctx)
        false_str = value_to_python(false_val, ctx)
        return f'If("{cond_name}", {true_str}, {false_str})'

    if intrinsic.type == IntrinsicType.EQUALS:
        ctx.add_intrinsic_import("Equals")
        val1, val2 = intrinsic.args
        str1 = value_to_python(val1, ctx)
        str2 = value_to_python(val2, ctx)
        return f"Equals({str1}, {str2})"

    if intrinsic.type == IntrinsicType.AND:
        ctx.add_intrinsic_import("And")
        conditions = [value_to_python(c, ctx) for c in intrinsic.args]
        return f"And(conditions=[{', '.join(conditions)}])"

    if intrinsic.type == IntrinsicType.OR:
        ctx.add_intrinsic_import("Or")
        conditions = [value_to_python(c, ctx) for c in intrinsic.args]
        return f"Or(conditions=[{', '.join(conditions)}])"

    if intrinsic.type == IntrinsicType.NOT:
        ctx.add_intrinsic_import("Not")
        cond_str = value_to_python(intrinsic.args, ctx)
        return f"Not({cond_str})"

    if intrinsic.type == IntrinsicType.CONDITION:
        ctx.add_intrinsic_import("Condition")
        return f'Condition("{intrinsic.args}")'

    if intrinsic.type == IntrinsicType.FIND_IN_MAP:
        ctx.add_intrinsic_import("FindInMap")
        map_name, top_key, second_key = intrinsic.args
        top_str = value_to_python(top_key, ctx)
        second_str = value_to_python(second_key, ctx)
        return f'FindInMap("{map_name}", {top_str}, {second_str})'

    if intrinsic.type == IntrinsicType.BASE64:
        ctx.add_intrinsic_import("Base64")
        val_str = value_to_python(intrinsic.args, ctx)
        return f"Base64({val_str})"

    if intrinsic.type == IntrinsicType.CIDR:
        ctx.add_intrinsic_import("Cidr")
        ip_block, count, cidr_bits = intrinsic.args
        block_str = value_to_python(ip_block, ctx)
        return f"Cidr({block_str}, {count}, {cidr_bits})"

    if intrinsic.type == IntrinsicType.IMPORT_VALUE:
        ctx.add_intrinsic_import("ImportValue")
        val_str = value_to_python(intrinsic.args, ctx)
        return f"ImportValue({val_str})"

    if intrinsic.type == IntrinsicType.SPLIT:
        ctx.add_intrinsic_import("Split")
        delimiter, source = intrinsic.args
        source_str = value_to_python(source, ctx)
        return f"Split({escape_string(delimiter)}, {source_str})"

    if intrinsic.type == IntrinsicType.VALUE_OF:
        ctx.add_intrinsic_import("ValueOf")
        param_name, attr_name = intrinsic.args
        param_str = value_to_python(param_name, ctx)
        attr_str = value_to_python(attr_name, ctx)
        return f"ValueOf({param_str}, {attr_str})"

    if intrinsic.type == IntrinsicType.TRANSFORM:
        ctx.add_intrinsic_import("Transform")
        args = intrinsic.args
        # Handle list form: Fn::Transform: [{Name: ..., Parameters: ...}]
        if isinstance(args, list) and len(args) == 1 and isinstance(args[0], dict):
            args = args[0]
        # Transform args is a dict with 'Name' and optionally 'Parameters'
        if isinstance(args, dict):
            name = args.get("Name", "")
            params = args.get("Parameters")
            name_str = escape_string(name) if isinstance(name, str) else value_to_python(name, ctx)
            if params:
                params_str = value_to_python(params, ctx)
                return f"Transform(name={name_str}, parameters={params_str})"
            return f"Transform(name={name_str})"
        # Fallback for unexpected format
        val_str = value_to_python(args, ctx)
        return f"Transform({val_str})"

    # Fallback
    return f"# Unknown intrinsic: {intrinsic.type}"
