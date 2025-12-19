"""Python code generation from IR."""

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Literal, Optional

from cloudformation_dataclasses.importer.ir import (
    IntrinsicType,
    IRCondition,
    IRIntrinsic,
    IRMapping,
    IROutput,
    IRParameter,
    IRProperty,
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
# Resource Type Registry
# =============================================================================

# Map resource types to (module, class_name)
# This is populated dynamically from aws modules
_RESOURCE_TYPE_MAP: dict[str, tuple[str, str]] = {}


def _build_resource_type_map() -> None:
    """Build mapping from CloudFormation types to Python classes."""
    global _RESOURCE_TYPE_MAP
    if _RESOURCE_TYPE_MAP:
        return  # Already built

    try:
        from cloudformation_dataclasses import aws

        for module_name in dir(aws):
            if module_name.startswith("_"):
                continue
            module = getattr(aws, module_name)
            if not hasattr(module, "__file__"):
                continue

            for class_name in dir(module):
                if class_name.startswith("_"):
                    continue
                cls = getattr(module, class_name)
                if hasattr(cls, "resource_type") and isinstance(cls.resource_type, str):
                    resource_type = cls.resource_type
                    _RESOURCE_TYPE_MAP[resource_type] = (module_name, class_name)
    except ImportError:
        pass  # AWS modules not available


def resolve_resource_type(resource_type: str) -> Optional[tuple[str, str]]:
    """
    Resolve a CloudFormation resource type to Python module and class.

    Returns:
        Tuple of (module_name, class_name) or None if unknown
    """
    _build_resource_type_map()
    return _RESOURCE_TYPE_MAP.get(resource_type)


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

    def add_import(self, module: str, name: str) -> None:
        """Add an import to track."""
        self.imports.setdefault(module, set()).add(name)

    def add_intrinsic_import(self, name: str) -> None:
        """Add an intrinsic function import."""
        self.intrinsic_imports.add(name)


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
            # Pseudo-parameter
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
            return f'Sub({_escape_string(intrinsic.args)})'
        template_str, variables = intrinsic.args
        if variables:
            vars_str = _value_to_python(variables, ctx)
            return f'Sub({_escape_string(template_str)}, {vars_str})'
        return f'Sub({_escape_string(template_str)})'

    if intrinsic.type == IntrinsicType.JOIN:
        ctx.add_intrinsic_import("Join")
        delimiter, values = intrinsic.args
        values_str = _value_to_python(values, ctx)
        return f'Join({_escape_string(delimiter)}, {values_str})'

    if intrinsic.type == IntrinsicType.SELECT:
        ctx.add_intrinsic_import("Select")
        index, list_val = intrinsic.args
        list_str = _value_to_python(list_val, ctx)
        return f"Select({index}, {list_str})"

    if intrinsic.type == IntrinsicType.GET_AZS:
        ctx.add_intrinsic_import("GetAZs")
        region = intrinsic.args
        if region:
            return f'GetAZs({_escape_string(region)})'
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
        return f'Split({_escape_string(delimiter)}, {source_str})'

    if intrinsic.type == IntrinsicType.TRANSFORM:
        ctx.add_intrinsic_import("Transform")
        val_str = _value_to_python(intrinsic.args, ctx)
        return f"Transform({val_str})"

    # Fallback
    return f"# Unknown intrinsic: {intrinsic.type}"


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

    # Type
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
    if resolved:
        module, class_name = resolved
        ctx.add_import(f"cloudformation_dataclasses.aws.{module}", class_name)
        lines.append(f"    resource: {class_name}")
    else:
        # Unknown resource type - use comment
        lines.append(f"    # Unknown resource type: {resource.resource_type}")
        lines.append("    resource: CloudFormationResource")
        ctx.add_import("cloudformation_dataclasses.core", "CloudFormationResource")

    # Properties
    for prop in resource.properties.values():
        value_str = _value_to_python(prop.value, ctx, indent=1)
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
        return f'Tag(key={_escape_string(key)}, value={_escape_string(value)})'


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
        isinstance(value, dict)
        and "Effect" in value
        and value.get("Effect") in ("Allow", "Deny")
    )


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
        condition_str = _value_to_python_mixed(condition, ctx, indent + 1)
        args.append(f"condition={condition_str}")

    if len(args) <= 2:
        return f"PolicyStatement({', '.join(args)})"
    else:
        args_str = f",\n{inner_indent}".join(args)
        return f"PolicyStatement(\n{inner_indent}{args_str},\n{indent_str})"


def _policy_document_to_python_mixed(doc: dict[str, Any], ctx: CodegenContext, indent: int = 0) -> str:
    """Convert a policy document dict to PolicyDocument code."""
    indent_str = "    " * indent
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


def _generate_template_class(template: IRTemplate, ctx: CodegenContext) -> str:
    """Generate the main template wrapper class."""
    lines = []

    # Determine class name from source file
    if template.source_file and template.source_file not in ("<string>", "<stream>"):
        # Extract name from path
        name = re.sub(r"[^a-zA-Z0-9]", "_", template.source_file.rsplit("/", 1)[-1].rsplit(".", 1)[0])
        name = "".join(word.title() for word in name.split("_"))
        class_name = f"{name}Template"
    else:
        class_name = "GeneratedTemplate"

    # Docstring
    if ctx.include_docstrings and template.description:
        lines.append(f'    """{template.description}"""')
        lines.append("")

    ctx.add_import("cloudformation_dataclasses.core", "Template")
    lines.append("    resource: Template")

    if template.description:
        lines.append(f"    description = {_escape_string(template.description)}")

    # Parameters
    if template.parameters:
        param_list = ", ".join(template.parameters.keys())
        lines.append(f"    parameters = [{param_list}]")

    # Resources
    if template.resources:
        resource_list = ", ".join(template.resources.keys())
        lines.append(f"    resources = [{resource_list}]")

    # Outputs
    if template.outputs:
        output_list = ", ".join(f"{lid}Output" for lid in template.outputs.keys())
        lines.append(f"    outputs = [{output_list}]")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    return f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines), class_name


# =============================================================================
# Brief Mode Generation (Imperative)
# =============================================================================


def _generate_parameter_imperative(param: IRParameter, ctx: CodegenContext) -> str:
    """Generate a parameter as an imperative instantiation."""
    ctx.add_import("cloudformation_dataclasses.core", "Parameter")

    args = [f'logical_id="{param.logical_id}"']
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
            lines.append(f"from cloudformation_dataclasses.intrinsics import {', '.join(sorted_intrinsics)}")
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
) -> str:
    """
    Generate Python code from analyzed IR.

    Args:
        template: Parsed IRTemplate
        mode: Output mode - "block" (declarative), "brief" (imperative), or "mixed"
        include_main: Include if __name__ == "__main__" block

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
        return _generate_brief_mode(template, ctx, sections, include_main)
    elif output_mode == OutputMode.MIXED:
        return _generate_mixed_mode(template, ctx, sections, include_main)
    else:
        return _generate_block_mode(template, ctx, sections, include_main)


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
    sorted_resources = _topological_sort(template)
    for resource_id in sorted_resources:
        resource = template.resources[resource_id]
        class_sections.append(_generate_resource_class(resource, ctx))

    # Outputs
    for output in template.outputs.values():
        class_sections.append(_generate_output_class(output, ctx))

    # Template class
    template_class, template_class_name = _generate_template_class(template, ctx)
    class_sections.append(template_class)

    # Now generate imports
    sections.append(_generate_imports(ctx))

    # Add class sections
    sections.extend(class_sections)

    # Build template function
    sections.append(f"""
def build_template() -> Template:
    \"\"\"Build the CloudFormation template.\"\"\"
    return {template_class_name}().resource""")

    # Main block
    if include_main:
        sections.append("""
if __name__ == "__main__":
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))""")

    return "\n\n\n".join(sections) + "\n"


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
        sections.append("""
if __name__ == "__main__":
    import json
    print(json.dumps(template.to_dict(), indent=2))""")

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

    # Template class
    template_class, template_class_name = _generate_template_class(template, ctx)
    class_sections.append(template_class)

    # Now generate imports
    sections.append(_generate_imports(ctx))

    # Add class sections
    sections.extend(class_sections)

    # Build template function
    sections.append(f"""
def build_template() -> Template:
    \"\"\"Build the CloudFormation template.\"\"\"
    return {template_class_name}().resource""")

    # Main block
    if include_main:
        sections.append("""
if __name__ == "__main__":
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))""")

    return "\n\n\n".join(sections) + "\n"
