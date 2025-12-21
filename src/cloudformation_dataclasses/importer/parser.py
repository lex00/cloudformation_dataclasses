"""CloudFormation template parser - YAML/JSON to IR."""

import json
import re
from pathlib import Path
from typing import Any, Optional, TextIO, Union

import yaml

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


# =============================================================================
# Name Conversion
# =============================================================================


def to_snake_case(name: str) -> str:
    """Convert PascalCase/camelCase to snake_case."""
    # Handle acronyms: VPCId -> vpc_id, IPv6 -> ipv6
    result = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    result = re.sub("([a-z0-9])([A-Z])", r"\1_\2", result)
    return result.lower()


def sanitize_python_name(name: str) -> str:
    """Handle Python keyword conflicts."""
    PYTHON_KEYWORDS = {
        "and",
        "as",
        "assert",
        "async",
        "await",
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
        "match",
        "case",
    }
    if name in PYTHON_KEYWORDS:
        return f"{name}_"
    return name


# =============================================================================
# YAML Intrinsic Constructors
# =============================================================================


def _ref_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Ref tag."""
    value = loader.construct_scalar(node)
    return IRIntrinsic(IntrinsicType.REF, value)


def _getatt_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !GetAtt tag (scalar or sequence)."""
    if isinstance(node, yaml.ScalarNode):
        # !GetAtt MyBucket.Arn
        value = loader.construct_scalar(node)
        parts = value.split(".", 1)
        return IRIntrinsic(IntrinsicType.GET_ATT, tuple(parts))
    else:
        # !GetAtt [MyBucket, Arn]
        parts = loader.construct_sequence(node)
        return IRIntrinsic(IntrinsicType.GET_ATT, tuple(parts))


def _sub_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Sub tag (scalar or sequence)."""
    if isinstance(node, yaml.ScalarNode):
        # !Sub "arn:aws:s3:::${BucketName}"
        value = loader.construct_scalar(node)
        return IRIntrinsic(IntrinsicType.SUB, value)
    else:
        # !Sub ["arn:aws:s3:::${Bucket}", {Bucket: !Ref MyBucket}]
        parts = loader.construct_sequence(node, deep=True)
        return IRIntrinsic(IntrinsicType.SUB, (parts[0], parts[1] if len(parts) > 1 else {}))


def _join_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Join tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.JOIN, (parts[0], parts[1]))


def _select_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Select tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.SELECT, (int(parts[0]), parts[1]))


def _getazs_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !GetAZs tag."""
    if isinstance(node, yaml.ScalarNode):
        value = loader.construct_scalar(node)
    elif isinstance(node, yaml.SequenceNode):
        value = loader.construct_sequence(node, deep=True)
        value = value[0] if value else ""
    else:  # MappingNode - e.g., !GetAZs { Ref: "AWS::Region" }
        value = loader.construct_mapping(node, deep=True)
    return IRIntrinsic(IntrinsicType.GET_AZS, value if value else "")


def _if_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !If tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.IF, tuple(parts[:3]))


def _equals_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Equals tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.EQUALS, tuple(parts[:2]))


def _and_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !And tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.AND, parts)


def _or_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Or tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.OR, parts)


def _not_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Not tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.NOT, parts[0])


def _condition_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Condition tag."""
    value = loader.construct_scalar(node)
    return IRIntrinsic(IntrinsicType.CONDITION, value)


def _findinmap_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !FindInMap tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.FIND_IN_MAP, tuple(parts[:3]))


def _base64_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Base64 tag."""
    if isinstance(node, yaml.ScalarNode):
        value = loader.construct_scalar(node)
    elif isinstance(node, yaml.SequenceNode):
        value = loader.construct_sequence(node, deep=True)
        value = value[0] if value else ""
    else:  # MappingNode - e.g., !Base64 { Fn::Sub: "..." }
        value = loader.construct_mapping(node, deep=True)
    return IRIntrinsic(IntrinsicType.BASE64, value)


def _cidr_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Cidr tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.CIDR, tuple(parts[:3]))


def _importvalue_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !ImportValue tag."""
    if isinstance(node, yaml.ScalarNode):
        value = loader.construct_scalar(node)
    elif isinstance(node, yaml.SequenceNode):
        value = loader.construct_sequence(node, deep=True)
        value = value[0] if value else ""
    else:  # MappingNode - e.g., !ImportValue { Fn::Sub: "..." }
        value = loader.construct_mapping(node, deep=True)
    return IRIntrinsic(IntrinsicType.IMPORT_VALUE, value)


def _split_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Split tag."""
    parts = loader.construct_sequence(node, deep=True)
    return IRIntrinsic(IntrinsicType.SPLIT, (parts[0], parts[1]))


def _transform_constructor(loader: yaml.SafeLoader, node: yaml.Node) -> IRIntrinsic:
    """Handle !Transform tag."""
    value = loader.construct_mapping(node, deep=True)
    return IRIntrinsic(IntrinsicType.TRANSFORM, value)


def _get_cfn_loader() -> type:
    """Create a YAML loader with CloudFormation intrinsic support."""

    class CloudFormationLoader(yaml.SafeLoader):
        pass

    # Register all intrinsic constructors
    CloudFormationLoader.add_constructor("!Ref", _ref_constructor)
    CloudFormationLoader.add_constructor("!GetAtt", _getatt_constructor)
    CloudFormationLoader.add_constructor("!Sub", _sub_constructor)
    CloudFormationLoader.add_constructor("!Join", _join_constructor)
    CloudFormationLoader.add_constructor("!Select", _select_constructor)
    CloudFormationLoader.add_constructor("!GetAZs", _getazs_constructor)
    CloudFormationLoader.add_constructor("!If", _if_constructor)
    CloudFormationLoader.add_constructor("!Equals", _equals_constructor)
    CloudFormationLoader.add_constructor("!And", _and_constructor)
    CloudFormationLoader.add_constructor("!Or", _or_constructor)
    CloudFormationLoader.add_constructor("!Not", _not_constructor)
    CloudFormationLoader.add_constructor("!Condition", _condition_constructor)
    CloudFormationLoader.add_constructor("!FindInMap", _findinmap_constructor)
    CloudFormationLoader.add_constructor("!Base64", _base64_constructor)
    CloudFormationLoader.add_constructor("!Cidr", _cidr_constructor)
    CloudFormationLoader.add_constructor("!ImportValue", _importvalue_constructor)
    CloudFormationLoader.add_constructor("!Split", _split_constructor)
    CloudFormationLoader.add_constructor("!Transform", _transform_constructor)

    return CloudFormationLoader


# =============================================================================
# Long-form Intrinsic Handling (JSON style)
# =============================================================================


def _resolve_long_form_intrinsics(value: Any) -> Any:
    """Convert Fn:: style intrinsics to IRIntrinsic objects."""
    if isinstance(value, IRIntrinsic):
        # Already converted (from YAML tags)
        return value

    if isinstance(value, dict):
        if len(value) == 1:
            key = next(iter(value))
            val = value[key]

            # Check for Ref
            if key == "Ref":
                return IRIntrinsic(IntrinsicType.REF, val)

            # Check for Fn:: prefix
            if key.startswith("Fn::"):
                intrinsic_name = key[4:]
                resolved_val = _resolve_long_form_intrinsics(val)

                if intrinsic_name == "GetAtt":
                    if isinstance(resolved_val, str):
                        parts = resolved_val.split(".", 1)
                    else:
                        parts = resolved_val
                    return IRIntrinsic(IntrinsicType.GET_ATT, tuple(parts))

                if intrinsic_name == "Sub":
                    if isinstance(resolved_val, str):
                        return IRIntrinsic(IntrinsicType.SUB, resolved_val)
                    return IRIntrinsic(
                        IntrinsicType.SUB,
                        (resolved_val[0], resolved_val[1] if len(resolved_val) > 1 else {}),
                    )

                if intrinsic_name == "Join":
                    return IRIntrinsic(IntrinsicType.JOIN, (resolved_val[0], resolved_val[1]))

                if intrinsic_name == "Select":
                    return IRIntrinsic(
                        IntrinsicType.SELECT, (int(resolved_val[0]), resolved_val[1])
                    )

                if intrinsic_name == "GetAZs":
                    return IRIntrinsic(IntrinsicType.GET_AZS, resolved_val if resolved_val else "")

                if intrinsic_name == "If":
                    return IRIntrinsic(IntrinsicType.IF, tuple(resolved_val[:3]))

                if intrinsic_name == "Equals":
                    return IRIntrinsic(IntrinsicType.EQUALS, tuple(resolved_val[:2]))

                if intrinsic_name == "And":
                    return IRIntrinsic(IntrinsicType.AND, resolved_val)

                if intrinsic_name == "Or":
                    return IRIntrinsic(IntrinsicType.OR, resolved_val)

                if intrinsic_name == "Not":
                    return IRIntrinsic(
                        IntrinsicType.NOT,
                        resolved_val[0] if isinstance(resolved_val, list) else resolved_val,
                    )

                if intrinsic_name == "FindInMap":
                    return IRIntrinsic(IntrinsicType.FIND_IN_MAP, tuple(resolved_val[:3]))

                if intrinsic_name == "Base64":
                    return IRIntrinsic(IntrinsicType.BASE64, resolved_val)

                if intrinsic_name == "Cidr":
                    return IRIntrinsic(IntrinsicType.CIDR, tuple(resolved_val[:3]))

                if intrinsic_name == "ImportValue":
                    return IRIntrinsic(IntrinsicType.IMPORT_VALUE, resolved_val)

                if intrinsic_name == "Split":
                    return IRIntrinsic(IntrinsicType.SPLIT, (resolved_val[0], resolved_val[1]))

                if intrinsic_name == "Transform":
                    return IRIntrinsic(IntrinsicType.TRANSFORM, resolved_val)

            # Check for Condition (used in resource Condition attribute)
            if key == "Condition":
                return IRIntrinsic(IntrinsicType.CONDITION, val)

        # Regular dict - recurse
        return {k: _resolve_long_form_intrinsics(v) for k, v in value.items()}

    if isinstance(value, list):
        return [_resolve_long_form_intrinsics(item) for item in value]

    return value


# =============================================================================
# Template Parsing
# =============================================================================


def _parse_parameter(logical_id: str, props: dict[str, Any]) -> IRParameter:
    """Parse a CloudFormation parameter."""
    return IRParameter(
        logical_id=logical_id,
        type=props.get("Type", "String"),
        description=props.get("Description"),
        default=props.get("Default"),
        allowed_values=props.get("AllowedValues"),
        allowed_pattern=props.get("AllowedPattern"),
        min_length=props.get("MinLength"),
        max_length=props.get("MaxLength"),
        min_value=props.get("MinValue"),
        max_value=props.get("MaxValue"),
        constraint_description=props.get("ConstraintDescription"),
        no_echo=props.get("NoEcho", False),
    )


def _parse_property(cf_name: str, value: Any) -> IRProperty:
    """Parse a single property into IR."""
    python_name = sanitize_python_name(to_snake_case(cf_name))
    resolved_value = _resolve_long_form_intrinsics(value)
    return IRProperty(cf_name=cf_name, python_name=python_name, value=resolved_value)


def _parse_resource(logical_id: str, resource_def: dict[str, Any]) -> IRResource:
    """Parse a CloudFormation resource."""
    resource_type = resource_def.get("Type", "")
    properties_raw = resource_def.get("Properties", {})

    properties = {}
    for cf_name, value in properties_raw.items():
        properties[cf_name] = _parse_property(cf_name, value)

    depends_on = resource_def.get("DependsOn", [])
    if isinstance(depends_on, str):
        depends_on = [depends_on]

    return IRResource(
        logical_id=logical_id,
        resource_type=resource_type,
        properties=properties,
        depends_on=depends_on,
        condition=resource_def.get("Condition"),
        deletion_policy=resource_def.get("DeletionPolicy"),
        update_replace_policy=resource_def.get("UpdateReplacePolicy"),
        metadata=resource_def.get("Metadata"),
    )


def _parse_output(logical_id: str, output_def: dict[str, Any]) -> IROutput:
    """Parse a CloudFormation output."""
    value = _resolve_long_form_intrinsics(output_def.get("Value"))
    export_name = output_def.get("Export", {}).get("Name")
    if export_name:
        export_name = _resolve_long_form_intrinsics(export_name)

    return IROutput(
        logical_id=logical_id,
        value=value,
        description=output_def.get("Description"),
        export_name=export_name,
        condition=output_def.get("Condition"),
    )


def _parse_mapping(logical_id: str, map_data: dict[str, dict[str, Any]]) -> IRMapping:
    """Parse a CloudFormation mapping."""
    return IRMapping(logical_id=logical_id, map_data=map_data)


def _parse_condition(logical_id: str, expression: Any) -> IRCondition:
    """Parse a CloudFormation condition."""
    resolved = _resolve_long_form_intrinsics(expression)
    return IRCondition(logical_id=logical_id, expression=resolved)


def parse_template(
    source: Union[str, Path, TextIO],
    source_name: Optional[str] = None,
) -> IRTemplate:
    """
    Parse a CloudFormation template into IR.

    Args:
        source: File path, string content, or file-like object
        source_name: Name for error messages (default: file path or "<stdin>")

    Returns:
        Parsed IRTemplate
    """
    # Determine content and source name
    if isinstance(source, Path):
        source_name = source_name or str(source)
        content = source.read_text()
    elif hasattr(source, "read"):
        source_name = source_name or "<stream>"
        content = source.read()
    else:
        source_name = source_name or "<string>"
        content = source

    # Check for unsupported custom tags
    if "!Rain::" in content:
        raise ValueError(
            "Template uses Rain-specific tags (!Rain::S3, etc.) which are not standard CloudFormation. "
            "These templates require the Rain CLI for preprocessing."
        )

    # Check for Kubernetes manifests (not CloudFormation templates)
    if "apiVersion:" in content and "kind:" in content:
        raise ValueError(
            "File appears to be a Kubernetes manifest, not a CloudFormation template."
        )

    # Try YAML first, fall back to JSON
    try:
        loader = _get_cfn_loader()
        data = yaml.load(content, Loader=loader)
    except yaml.YAMLError:
        try:
            data = json.loads(content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse template: {e}") from e

    if not isinstance(data, dict):
        raise ValueError("Template must be a dictionary/object")

    # Build IR
    template = IRTemplate(
        description=data.get("Description"),
        aws_template_format_version=data.get("AWSTemplateFormatVersion", "2010-09-09"),
        source_file=source_name,
    )

    # Parse parameters
    for logical_id, param_def in data.get("Parameters", {}).items():
        template.parameters[logical_id] = _parse_parameter(logical_id, param_def)

    # Parse mappings
    for logical_id, map_data in data.get("Mappings", {}).items():
        template.mappings[logical_id] = _parse_mapping(logical_id, map_data)

    # Parse conditions
    for logical_id, expression in data.get("Conditions", {}).items():
        template.conditions[logical_id] = _parse_condition(logical_id, expression)

    # Parse resources
    for logical_id, resource_def in data.get("Resources", {}).items():
        template.resources[logical_id] = _parse_resource(logical_id, resource_def)

    # Parse outputs
    for logical_id, output_def in data.get("Outputs", {}).items():
        template.outputs[logical_id] = _parse_output(logical_id, output_def)

    # Build reference graph
    _analyze_references(template)

    return template


def _analyze_references(template: IRTemplate) -> None:
    """Populate reference_graph by analyzing Ref/GetAtt usage."""

    def find_refs(value: Any, source_id: str) -> None:
        if isinstance(value, IRIntrinsic):
            if value.type == IntrinsicType.REF:
                target_id = value.args
                template.reference_graph.setdefault(source_id, []).append(target_id)
            elif value.type == IntrinsicType.GET_ATT:
                target_id = value.args[0]
                template.reference_graph.setdefault(source_id, []).append(target_id)
            elif value.type == IntrinsicType.SUB:
                # Parse ${Var} and ${Var.Attr} from Sub strings
                if isinstance(value.args, str):
                    sub_str = value.args
                else:
                    sub_str = value.args[0]
                # Find all ${...} patterns
                for match in re.finditer(r"\$\{([^}]+)\}", sub_str):
                    ref_name = match.group(1).split(".")[0]
                    # Skip AWS:: pseudo parameters
                    if not ref_name.startswith("AWS::"):
                        template.reference_graph.setdefault(source_id, []).append(ref_name)
            # Recurse into intrinsic args
            if isinstance(value.args, (list, tuple)):
                for item in value.args:
                    find_refs(item, source_id)
            elif isinstance(value.args, dict):
                for v in value.args.values():
                    find_refs(v, source_id)
        elif isinstance(value, dict):
            for v in value.values():
                find_refs(v, source_id)
        elif isinstance(value, list):
            for item in value:
                find_refs(item, source_id)

    for resource_id, resource in template.resources.items():
        for prop in resource.properties.values():
            find_refs(prop.value, resource_id)

    for output_id, output in template.outputs.items():
        find_refs(output.value, output_id)
