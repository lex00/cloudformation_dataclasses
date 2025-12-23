"""Python code generation from IR."""

import datetime
import re
from dataclasses import dataclass, field
from typing import Any, Optional

from cloudformation_dataclasses.constants import (
    CONDITION_OPERATOR_MAP,
    PARAMETER_TYPE_MAP,
    PSEUDO_PARAMETER_MAP,
    find_property_type_for_cf_keys,
    get_property_type_info,
    is_ambiguous_class_name,
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


# =============================================================================
# Service Category Mapping for Resource File Organization
# =============================================================================

# Map AWS service names to category files for large templates (10+ resources)
SERVICE_CATEGORIES: dict[str, str] = {
    # Compute
    "EC2": "compute",
    "Lambda": "compute",
    "ECS": "compute",
    "EKS": "compute",
    "Batch": "compute",
    "AutoScaling": "compute",
    "ElasticBeanstalk": "compute",
    "Lightsail": "compute",
    # Storage
    "S3": "storage",
    "EFS": "storage",
    "FSx": "storage",
    "Backup": "storage",
    # Database
    "RDS": "database",
    "DynamoDB": "database",
    "ElastiCache": "database",
    "Neptune": "database",
    "DocumentDB": "database",
    "Redshift": "database",
    "MemoryDB": "database",
    # Networking
    "ElasticLoadBalancing": "network",
    "ElasticLoadBalancingV2": "network",
    "Route53": "network",
    "CloudFront": "network",
    "APIGateway": "network",
    "ApiGatewayV2": "network",
    "GlobalAccelerator": "network",
    # Security/IAM
    "IAM": "security",
    "Cognito": "security",
    "SecretsManager": "security",
    "KMS": "security",
    "WAF": "security",
    "WAFv2": "security",
    "ACM": "security",
    "SSM": "security",
    # Messaging/Integration
    "SNS": "messaging",
    "SQS": "messaging",
    "EventBridge": "messaging",
    "Events": "messaging",
    "StepFunctions": "messaging",
    "AppSync": "messaging",
    # Monitoring/Logging
    "CloudWatch": "monitoring",
    "Logs": "monitoring",
    "CloudTrail": "monitoring",
    "XRay": "monitoring",
    # CI/CD
    "CodeBuild": "cicd",
    "CodePipeline": "cicd",
    "CodeCommit": "cicd",
    "CodeDeploy": "cicd",
    # Infrastructure
    "CloudFormation": "infra",
    "Config": "infra",
    "ServiceCatalog": "infra",
}

# EC2 resource types that should go to network.py instead of compute.py
EC2_NETWORK_TYPES: set[str] = {
    "VPC",
    "Subnet",
    "InternetGateway",
    "NatGateway",
    "RouteTable",
    "Route",
    "SecurityGroup",
    "NetworkAcl",
    "VPCEndpoint",
    "EIP",
    "VPCGatewayAttachment",
    "SubnetRouteTableAssociation",
    "NetworkInterface",
    "VPNGateway",
    "VPNConnection",
    "CustomerGateway",
    "TransitGateway",
    "TransitGatewayAttachment",
}


def _get_resource_category(resource: IRResource) -> str:
    """Get the category file for a resource based on its AWS service.

    Returns 'main' for uncategorized services, or a category name like
    'compute', 'storage', 'network', etc.
    """
    service = resource.service

    # Special case: EC2 VPC-related resources go to network
    if service == "EC2" and resource.type_name in EC2_NETWORK_TYPES:
        return "network"

    return SERVICE_CATEGORIES.get(service, "main")


# =============================================================================
# Helpers
# =============================================================================


def _sanitize_class_name(name: str) -> str:
    """Ensure name is a valid Python identifier.

    CloudFormation allows logical IDs starting with digits, but Python
    class names cannot start with digits. Prepend underscore if needed.
    """
    if name and name[0].isdigit():
        return f"_{name}"
    return name


def _resolve_property_type(
    expected_class: Optional[str],
    expected_module: Optional[str],
    cf_keys: Optional[set[str]] = None,
    module_hint: Optional[str] = None,
) -> Optional[tuple[str, str, dict[str, Any]]]:
    """
    Resolve a PropertyType by expected class/module or by CF property keys.

    First tries to match using expected_class and expected_module.
    If that fails, falls back to searching by CF property keys.

    Args:
        expected_class: Expected class name from type hint
        expected_module: Expected module name from type hint
        cf_keys: Set of CloudFormation property names in the dict
        module_hint: Module hint for key-based lookup (e.g., "ec2")

    Returns:
        Tuple of (module_name, class_name, property_type_info) or None if not found.
    """
    # Try expected class first
    if expected_class and expected_module:
        info = get_property_type_info(expected_module, expected_class)
        if info:
            return (expected_module, expected_class, info)

    # Fall back to key-based lookup
    if cf_keys:
        match = find_property_type_for_cf_keys(cf_keys, module_hint=module_hint)
        if match:
            pt_module, pt_class = match
            info = get_property_type_info(pt_module, pt_class)
            if info:
                return (pt_module, pt_class, info)

    return None


# =============================================================================
# Annotated Field Value (for annotation-based refs)
# =============================================================================


@dataclass
class AnnotatedValue:
    """
    Represents a field value that needs a type annotation.

    Used for annotation-based refs like: bucket: Ref[Bucket] = ref()
    Instead of: bucket = ref("Bucket")
    """

    annotation: str  # e.g., "Ref[Bucket]"
    value: str  # e.g., "ref()"


# =============================================================================
# Code Generation Context
# =============================================================================


@dataclass
class CodegenContext:
    """Context for code generation."""

    template: IRTemplate
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

    # Map of Sub template patterns to resource logical IDs (for implicit ref detection)
    # e.g., "${AppName}-${AWS::Region}-${AWS::AccountId}" -> "ObjectStorageBucket"
    name_pattern_map: dict[str, str] = field(default_factory=dict)

    # Map of ARN Sub patterns to (resource_id, suffix) for get_att() replacement
    # e.g., "arn:${AWS::Partition}:s3:::${bucket-name}" -> ("BucketResource", "")
    # e.g., "arn:${AWS::Partition}:s3:::${bucket-name}/*" -> ("BucketResource", "/*")
    arn_pattern_map: dict[str, tuple[str, str]] = field(default_factory=dict)

    # Current resource ID being generated (to avoid self-referential ref() replacements)
    current_resource_id: Optional[str] = None

    # AWS class names that collide across modules (e.g., 'Policy' from both iam and iot)
    # These need qualified access like iot.Policy instead of bare Policy
    colliding_aws_names: dict[str, str] = field(default_factory=dict)  # name -> module

    # Set of resource IDs that are forward references (defined later in same SCC file)
    # For these, use string-based refs like ref("MyLambdaRole") instead of ref(MyLambdaRole)
    forward_references: set[str] = field(default_factory=set)

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


# Properties that define a resource's "name" for implicit ref detection
NAME_PROPERTIES = frozenset([
    "BucketName",      # S3
    "RoleName",        # IAM
    "TableName",       # DynamoDB
    "FunctionName",    # Lambda
    "QueueName",       # SQS
    "TopicName",       # SNS
    "StackName",       # CloudFormation
    "ClusterName",     # ECS, EKS, etc.
    "LogGroupName",    # CloudWatch Logs
    "StreamName",      # Kinesis
    "DatabaseName",    # RDS, Glue
    "RepositoryName",  # ECR
    "VaultName",       # Glacier
    "DomainName",      # Various services
    "Name",            # Generic fallback
])


def _build_name_pattern_map(template: IRTemplate) -> dict[str, str]:
    """Build a map of Sub template patterns to resource logical IDs.

    This enables detecting when a Sub pattern matches a resource's name,
    allowing replacement with ref() for proper dependency tracking.

    For example, if:
    - ObjectStorageBucket has BucketName: !Sub "${AppName}-${AWS::Region}-${AWS::AccountId}"
    - ObjectStorageBucketPolicy has Bucket: !Sub "${AppName}-${AWS::Region}-${AWS::AccountId}"

    We can detect the match and generate:
    - bucket = ref(ObjectStorageBucket)
    instead of:
    - bucket = Sub("${AppName}-${AWS::Region}-${AWS::AccountId}")

    Returns:
        Dict mapping Sub template strings to resource logical IDs
    """
    pattern_map: dict[str, str] = {}

    for logical_id, resource in template.resources.items():
        for prop_cf_name in NAME_PROPERTIES:
            if prop_cf_name in resource.properties:
                prop = resource.properties[prop_cf_name]
                # Check if it's a Sub intrinsic
                if isinstance(prop.value, IRIntrinsic) and prop.value.type == IntrinsicType.SUB:
                    # Extract the template string
                    if isinstance(prop.value.args, str):
                        template_str = prop.value.args
                    elif isinstance(prop.value.args, (list, tuple)) and len(prop.value.args) >= 1:
                        template_str = prop.value.args[0]
                    else:
                        continue
                    # Store the mapping (first occurrence wins)
                    if template_str not in pattern_map:
                        pattern_map[template_str] = logical_id

    return pattern_map


# ARN prefix patterns by CloudFormation resource type
# These define the ARN structure before the resource name for each service
ARN_PREFIX_PATTERNS: dict[str, str] = {
    "AWS::S3::Bucket": "arn:${AWS::Partition}:s3:::",
    "AWS::IAM::Role": "arn:${AWS::Partition}:iam::${AWS::AccountId}:role/",
    "AWS::IAM::Policy": "arn:${AWS::Partition}:iam::${AWS::AccountId}:policy/",
    "AWS::Lambda::Function": "arn:${AWS::Partition}:lambda:${AWS::Region}:${AWS::AccountId}:function:",
    "AWS::DynamoDB::Table": "arn:${AWS::Partition}:dynamodb:${AWS::Region}:${AWS::AccountId}:table/",
    "AWS::SQS::Queue": "arn:${AWS::Partition}:sqs:${AWS::Region}:${AWS::AccountId}:",
    "AWS::SNS::Topic": "arn:${AWS::Partition}:sns:${AWS::Region}:${AWS::AccountId}:",
    "AWS::Logs::LogGroup": "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:",
    "AWS::Kinesis::Stream": "arn:${AWS::Partition}:kinesis:${AWS::Region}:${AWS::AccountId}:stream/",
    "AWS::KMS::Key": "arn:${AWS::Partition}:kms:${AWS::Region}:${AWS::AccountId}:key/",
    "AWS::ECR::Repository": "arn:${AWS::Partition}:ecr:${AWS::Region}:${AWS::AccountId}:repository/",
    "AWS::ECS::Cluster": "arn:${AWS::Partition}:ecs:${AWS::Region}:${AWS::AccountId}:cluster/",
    "AWS::StepFunctions::StateMachine": "arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:stateMachine:",
    "AWS::Events::Rule": "arn:${AWS::Partition}:events:${AWS::Region}:${AWS::AccountId}:rule/",
    "AWS::SecretsManager::Secret": "arn:${AWS::Partition}:secretsmanager:${AWS::Region}:${AWS::AccountId}:secret:",
    "AWS::SSM::Parameter": "arn:${AWS::Partition}:ssm:${AWS::Region}:${AWS::AccountId}:parameter/",
}


def _build_arn_pattern_map(template: IRTemplate) -> dict[str, tuple[str, str]]:
    """Build a map of ARN Sub patterns to (resource_id, suffix).

    This enables detecting when a Sub pattern builds an ARN that matches
    a resource's name pattern, allowing replacement with get_att(Resource, "Arn").

    For example, if ObjectStorageBucket has:
        BucketName: !Sub "${AppName}-${AWS::Region}-${AWS::AccountId}"

    Then these ARN patterns will match:
        "arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}" -> ("ObjectStorageBucket", "")
        "arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*" -> ("ObjectStorageBucket", "/*")

    Returns:
        Dict mapping ARN template strings to (resource_logical_id, suffix) tuples
    """
    arn_map: dict[str, tuple[str, str]] = {}

    for logical_id, resource in template.resources.items():
        # Get the ARN prefix for this resource type
        arn_prefix = ARN_PREFIX_PATTERNS.get(resource.resource_type)
        if not arn_prefix:
            continue

        # Find the resource's name pattern
        for prop_cf_name in NAME_PROPERTIES:
            if prop_cf_name in resource.properties:
                prop = resource.properties[prop_cf_name]
                if isinstance(prop.value, IRIntrinsic) and prop.value.type == IntrinsicType.SUB:
                    # Extract the template string
                    if isinstance(prop.value.args, str):
                        name_pattern = prop.value.args
                    elif isinstance(prop.value.args, (list, tuple)) and len(prop.value.args) >= 1:
                        name_pattern = prop.value.args[0]
                    else:
                        continue

                    # Build the full ARN pattern
                    full_arn = f"{arn_prefix}{name_pattern}"

                    # Store exact match (first occurrence wins)
                    if full_arn not in arn_map:
                        arn_map[full_arn] = (logical_id, "")

                    # Also store common wildcard variants
                    wildcard_arn = f"{full_arn}/*"
                    if wildcard_arn not in arn_map:
                        arn_map[wildcard_arn] = (logical_id, "/*")

    return arn_map


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
        result = _intrinsic_to_python(value, ctx)
        # AnnotatedValue is only for top-level properties, not inline values
        if isinstance(result, AnnotatedValue):
            return _annotated_to_class_ref(result)
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

        resolved = _resolve_property_type(
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
        if '"""' not in s:
            return f'"""{s}"""'
        # Contains triple double quotes - try triple single quotes
        if "'''" not in s:
            return f"'''{s}'''"
        # Both quote styles present - fall back to repr
        return repr(s)
    return repr(s)


def _escape_docstring(s: str) -> str:
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


def _annotated_to_class_ref(annotated: AnnotatedValue) -> str:
    """Convert an AnnotatedValue to a class-based ref for inline use.

    AnnotatedValue is for top-level properties only. When used inline
    (in lists, dicts, etc.), we use class-based refs like ref(ClassName).
    """
    import re

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


def _value_to_python(
    value: Any,
    ctx: CodegenContext,
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
    indent_str = "    " * indent

    if isinstance(value, IRIntrinsic):
        result = _intrinsic_to_python(value, ctx)
        # AnnotatedValue is only for top-level properties, not inline values
        if isinstance(result, AnnotatedValue):
            return _annotated_to_class_ref(result)
        return result

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
            return f"[{_value_to_python(value[0], ctx, indent, parent_property_type, use_property_type_keys)}]"
        items = [_value_to_python(item, ctx, indent + 1, parent_property_type, use_property_type_keys) for item in value]
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
                key_str = _escape_string(k) if isinstance(k, str) else str(k)

            # For nested dicts, determine the child PropertyType from the key name
            child_property_type = None
            if isinstance(v, (dict, list)) and module_hint:
                child_info = get_property_type_info(module_hint, k)
                if child_info:
                    child_property_type = (module_hint, k)

            val_str = _value_to_python(v, ctx, indent + 1, child_property_type, use_property_type_keys)
            items.append(f"{key_str}: {val_str}")
        inner = f",\n{indent_str}    ".join(items)
        return f"{{\n{indent_str}    {inner},\n{indent_str}}}"

    return repr(value)


def _intrinsic_to_python(intrinsic: IRIntrinsic, ctx: CodegenContext) -> str | AnnotatedValue:
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
            # Region can be a string or an intrinsic like !Ref AWS::Region
            if isinstance(region, IRIntrinsic):
                region_str = _intrinsic_to_python(region, ctx)
                return f"GetAZs({region_str})"
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
        return f"And(conditions=[{', '.join(conditions)}])"

    if intrinsic.type == IntrinsicType.OR:
        ctx.add_intrinsic_import("Or")
        conditions = [_value_to_python(c, ctx) for c in intrinsic.args]
        return f"Or(conditions=[{', '.join(conditions)}])"

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

    if intrinsic.type == IntrinsicType.VALUE_OF:
        ctx.add_intrinsic_import("ValueOf")
        param_name, attr_name = intrinsic.args
        param_str = _value_to_python(param_name, ctx)
        attr_str = _value_to_python(attr_name, ctx)
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
            name_str = _escape_string(name) if isinstance(name, str) else _value_to_python(name, ctx)
            if params:
                params_str = _value_to_python(params, ctx)
                return f"Transform(name={name_str}, parameters={params_str})"
            return f"Transform(name={name_str})"
        # Fallback for unexpected format
        val_str = _value_to_python(args, ctx)
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
) -> str | AnnotatedValue:
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
            item_result = _property_value_to_python_block(
                item,
                parent_logical_id,
                f"{property_path}.{i}",
                f"Optional[{inner_class}]" if inner_class else expected_type,
                expected_module,
                ctx,
            )
            # AnnotatedValue is only for top-level properties, not inside lists
            if isinstance(item_result, AnnotatedValue):
                item_str = _annotated_to_class_ref(item_result)
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
        expected_class = _extract_class_from_type_hint(expected_type)
        cf_keys = set(value.keys())

        resolved = _resolve_property_type(
            expected_class, expected_module, cf_keys, module_hint=expected_module
        )

        if resolved:
            pt_module, pt_class, _ = resolved
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
            val_result = _property_value_to_python_block(
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
            val_str = _value_to_python(val, ctx, indent=1)
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
    # Note: YAML may parse "2012-10-17" as a datetime.date, so convert to string
    version = doc.get("Version", "2012-10-17")
    if isinstance(version, (datetime.date, datetime.datetime)):
        version = version.strftime("%Y-%m-%d")
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
        lines.append(f'    {_escape_docstring(param.description)}')
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

    class_name = _sanitize_class_name(param.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)


def _generate_resource_class(resource: IRResource, ctx: CodegenContext) -> str:
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

        value_result = _property_value_to_python_block(
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
        lines.append(f"    condition = {_escape_string(resource.condition)}")
    if resource.deletion_policy:
        lines.append(f"    deletion_policy = {_escape_string(resource.deletion_policy)}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    class_name = _sanitize_class_name(resource.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}:\n" + "\n".join(lines)


def _generate_output_class(output: IROutput, ctx: CodegenContext) -> str:
    """Generate an output wrapper class."""
    lines = []

    # Docstring
    if ctx.include_docstrings and output.description:
        lines.append(f'    {_escape_docstring(output.description)}')
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

    class_name = _sanitize_class_name(output.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}Output:\n" + "\n".join(lines)


def _generate_mapping_class(mapping: IRMapping, ctx: CodegenContext) -> str:
    """Generate a mapping wrapper class."""
    lines = []

    ctx.add_import("cloudformation_dataclasses.core", "Mapping")
    lines.append("    resource: Mapping")

    # Map data as dict - disable PropertyType keys since mapping data is user-defined
    map_str = _value_to_python(mapping.map_data, ctx, indent=1, use_property_type_keys=False)
    lines.append(f"    map_data = {map_str}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    class_name = _sanitize_class_name(mapping.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}Mapping:\n" + "\n".join(lines)


def _generate_condition_class(condition: IRCondition, ctx: CodegenContext) -> str:
    """Generate a condition wrapper class."""
    lines = []

    ctx.add_import("cloudformation_dataclasses.core", "Condition")
    lines.append("    resource: Condition")

    # Expression
    expr_str = _value_to_python(condition.expression, ctx, indent=1)
    lines.append(f"    expression = {expr_str}")

    ctx.add_import("cloudformation_dataclasses.core", "cloudformation_dataclass")

    class_name = _sanitize_class_name(condition.logical_id)
    return f"@cloudformation_dataclass\nclass {class_name}Condition:\n" + "\n".join(lines)


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

        val_str = _value_to_python(conditions, ctx, indent + 1)
        items.append(f"{key_str}: {val_str}")

    inner = f",\n{indent_str}    ".join(items)
    return f"{{\n{indent_str}    {inner},\n{indent_str}}}"


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
# Topological Sort and Cycle Detection
# =============================================================================


def _find_strongly_connected_components(template: IRTemplate) -> list[list[str]]:
    """Find strongly connected components using Tarjan's algorithm.

    Returns a list of SCCs, where each SCC is a list of resource IDs.
    Resources in the same SCC form a cycle and should be in the same file.
    SCCs are returned in reverse topological order (dependencies first).
    """
    # Only consider resources (not parameters, etc.)
    resources = set(template.resources.keys())

    # Build pattern maps for implicit ref/get_att detection
    # These are needed to find dependencies created during code generation
    name_pattern_map = _build_name_pattern_map(template)
    arn_pattern_map = _build_arn_pattern_map(template)

    # Build adjacency list for resources only, including implicit dependencies
    graph: dict[str, list[str]] = {}
    for resource_id in resources:
        deps = _find_resource_dependencies(
            template, resource_id, name_pattern_map, arn_pattern_map
        )
        graph[resource_id] = [d for d in deps if d in resources]

    # Tarjan's algorithm
    index_counter = [0]
    stack: list[str] = []
    lowlinks: dict[str, int] = {}
    index: dict[str, int] = {}
    on_stack: set[str] = set()
    sccs: list[list[str]] = []

    def strongconnect(node: str) -> None:
        index[node] = index_counter[0]
        lowlinks[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        on_stack.add(node)

        for successor in graph.get(node, []):
            if successor not in index:
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node], lowlinks[successor])
            elif successor in on_stack:
                lowlinks[node] = min(lowlinks[node], index[successor])

        # If node is a root node, pop the stack and generate an SCC
        if lowlinks[node] == index[node]:
            scc: list[str] = []
            while True:
                successor = stack.pop()
                on_stack.remove(successor)
                scc.append(successor)
                if successor == node:
                    break
            sccs.append(scc)

    for node in resources:
        if node not in index:
            strongconnect(node)

    return sccs


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
    include_main: bool = True,
) -> str:
    """
    Generate Python code from analyzed IR.

    Args:
        template: Parsed IRTemplate
        include_main: Include if __name__ == "__main__" block

    Returns:
        Complete Python module source code
    """
    ctx = CodegenContext(
        template=template,
        include_main_block=include_main,
    )

    # Build pattern maps for implicit ref and get_att detection
    ctx.name_pattern_map = _build_name_pattern_map(template)
    ctx.arn_pattern_map = _build_arn_pattern_map(template)

    # Add ref and get_att imports (commonly needed)
    ctx.add_import("cloudformation_dataclasses.core", "ref")
    ctx.add_import("cloudformation_dataclasses.core", "get_att")

    sections: list[str] = []

    # Module docstring
    if template.description:
        sections.append(f'"""\n{template.description}\n\nGenerated by cfn-dataclasses-import.\n"""')
    else:
        sections.append('"""Generated by cfn-dataclasses-import."""')

    code = _generate_block_mode(template, ctx, sections, include_main)

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

    # Per-file imports
    init_imports: dict[str, set[str]] = field(default_factory=dict)
    config_classes: list[str] = field(default_factory=list)
    resources_classes: list[str] = field(default_factory=list)
    main_classes: list[str] = field(default_factory=list)

    # Cross-file references (for explicit imports)
    # Maps: file -> set of class names from other files it references
    config_exports: set[str] = field(default_factory=set)
    resources_exports: set[str] = field(default_factory=set)
    outputs_exports: set[str] = field(default_factory=set)

    # For generating classes, we need a CodegenContext
    codegen_ctx: CodegenContext = field(default=None)

    def __post_init__(self):
        if self.codegen_ctx is None:
            self.codegen_ctx = CodegenContext(template=self.template)
            # Build pattern maps for implicit ref and get_att detection
            self.codegen_ctx.name_pattern_map = _build_name_pattern_map(self.template)
            self.codegen_ctx.arn_pattern_map = _build_arn_pattern_map(self.template)


def _generate_init_py(pkg_ctx: PackageContext, template: IRTemplate) -> str:
    """Generate __init__.py with centralized imports."""
    lines = []

    # Docstring from template description
    if template.description:
        # Truncate long descriptions
        desc = template.description.strip()
        if len(desc) > 200:
            desc = desc[:197] + "..."
        lines.append(f'"""{desc}\n\nGenerated by cfn-dataclasses-import."""')
    else:
        lines.append('"""Generated by cfn-dataclasses-import."""')

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
        if len(sorted_imports) <= 3:
            lines.append(
                f"from cloudformation_dataclasses.core import {', '.join(sorted_imports)}"
            )
        else:
            lines.append("from cloudformation_dataclasses.core import (")
            for name in sorted_imports:
                lines.append(f"    {name},")
            lines.append(")")

    # AWS module imports (e.g., from cloudformation_dataclasses.aws import s3)
    # This is needed when wrapper class names collide with AWS resource class names
    aws_base = ctx.imports.get("cloudformation_dataclasses.aws", set())
    if aws_base:
        sorted_modules = sorted(aws_base)
        if len(sorted_modules) <= 3:
            lines.append(
                f"from cloudformation_dataclasses.aws import {', '.join(sorted_modules)}"
            )
        else:
            lines.append("from cloudformation_dataclasses.aws import (")
            for name in sorted_modules:
                lines.append(f"    {name},")
            lines.append(")")

    # AWS submodule imports (e.g., from cloudformation_dataclasses.aws.s3 import Bucket)
    aws_modules = sorted(
        (mod, names)
        for mod, names in ctx.imports.items()
        if mod.startswith("cloudformation_dataclasses.aws.")
    )

    # Detect name collisions across AWS modules
    # When multiple modules export the same name (e.g., Policy from iam and iot),
    # we need to use qualified imports instead of direct imports
    all_aws_names: dict[str, list[str]] = {}
    for module, names in aws_modules:
        for name in names:
            all_aws_names.setdefault(name, []).append(module)

    colliding_names = {name for name, mods in all_aws_names.items() if len(mods) > 1}

    # Store colliding names in context so resource file codegen can use qualified access
    # Map each colliding name to its module (for cases where we know which module to use)
    for name in colliding_names:
        for mod in all_aws_names[name]:
            short_mod = mod.split(".")[-1]  # e.g., 'iot' from '...aws.iot'
            # Store name -> module mapping for use in resource codegen
            # If multiple modules have the same name, store all of them
            ctx.colliding_aws_names[name] = short_mod  # Last one wins, but we also track in aws_base

    # For colliding names, add their modules to aws_base for qualified access
    if colliding_names:
        if aws_base is None:
            aws_base = set()
        for name in colliding_names:
            for mod in all_aws_names[name]:
                short_mod = mod.split(".")[-1]  # e.g., 'iot' from '...aws.iot'
                aws_base.add(short_mod)

        # Re-emit aws_base imports if we added new modules
        # (only if we didn't already emit them above)
        if not ctx.imports.get("cloudformation_dataclasses.aws"):
            sorted_modules = sorted(aws_base)
            if len(sorted_modules) <= 3:
                lines.append(
                    f"from cloudformation_dataclasses.aws import {', '.join(sorted_modules)}"
                )
            else:
                lines.append("from cloudformation_dataclasses.aws import (")
                for name in sorted_modules:
                    lines.append(f"    {name},")
                lines.append(")")

    for module, names in aws_modules:
        # Only import non-colliding names directly
        direct_names = sorted(n for n in names if n not in colliding_names)
        if direct_names:
            if len(direct_names) <= 3:
                lines.append(f"from {module} import {', '.join(direct_names)}")
            else:
                lines.append(f"from {module} import (")
                for name in direct_names:
                    lines.append(f"    {name},")
                lines.append(")")

    # Intrinsic imports
    if ctx.intrinsic_imports:
        sorted_intrinsics = sorted(ctx.intrinsic_imports)
        if len(sorted_intrinsics) <= 3:
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

    # Re-export everything from .stack (params, outputs, resources)
    # This provides `from packagename import ResourceName` access
    lines.append("from .stack import *  # noqa: F403, F401")
    lines.append("")

    # Collect names for __all__
    config_names: list[str] = []
    for param in template.parameters.values():
        config_names.append(_sanitize_class_name(param.logical_id))
    for mapping in template.mappings.values():
        config_names.append(f"{_sanitize_class_name(mapping.logical_id)}Mapping")
    for condition in template.conditions.values():
        config_names.append(f"{_sanitize_class_name(condition.logical_id)}Condition")

    resource_names: list[str] = []
    for resource in template.resources.values():
        resource_names.append(_sanitize_class_name(resource.logical_id))

    output_names: list[str] = []
    for output in template.outputs.values():
        output_names.append(f"{_sanitize_class_name(output.logical_id)}Output")

    # Generate __all__ with all exported names
    # Exclude colliding names - they're accessed via module (e.g., iot.Policy)
    direct_aws_names = set().union(*[names for _, names in aws_modules]) - colliding_names
    all_names = sorted(core_imports | direct_aws_names)
    # Add AWS module names (e.g., 's3') for qualified access like s3.Bucket
    if aws_base:
        all_names = sorted(set(all_names) | aws_base)
    if ctx.intrinsic_imports:
        all_names = sorted(set(all_names) | ctx.intrinsic_imports)
    # Add config names to __all__
    all_names = sorted(set(all_names) | set(config_names))
    # Add resource names to __all__
    all_names = sorted(set(all_names) | set(resource_names))
    # Add output names to __all__
    all_names = sorted(set(all_names) | set(output_names))

    lines.append("__all__ = [")
    for name in all_names:
        lines.append(f'    "{name}",')
    lines.append("]")

    return "\n".join(lines) + "\n"


def _generate_params_py(pkg_ctx: PackageContext, template: IRTemplate) -> str:
    """Generate stack/params.py with Parameters, Mappings, Conditions."""
    lines = []
    lines.append('"""Parameters, Mappings, and Conditions."""')
    lines.append("")
    lines.append("from .. import *  # noqa: F403")
    lines.append("")
    lines.append("")

    ctx = pkg_ctx.codegen_ctx

    # Parameters
    for param in template.parameters.values():
        class_def = _generate_parameter_class(param, ctx)
        lines.append(class_def)
        lines.append("")
        lines.append("")
        pkg_ctx.config_exports.add(_sanitize_class_name(param.logical_id))

    # Mappings
    for mapping in template.mappings.values():
        class_def = _generate_mapping_class(mapping, ctx)
        lines.append(class_def)
        lines.append("")
        lines.append("")
        pkg_ctx.config_exports.add(f"{_sanitize_class_name(mapping.logical_id)}Mapping")

    # Conditions
    for condition in template.conditions.values():
        class_def = _generate_condition_class(condition, ctx)
        lines.append(class_def)
        lines.append("")
        lines.append("")
        pkg_ctx.config_exports.add(f"{_sanitize_class_name(condition.logical_id)}Condition")

    # Remove trailing empty lines
    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines) + "\n"


def _generate_resources_py(pkg_ctx: PackageContext, template: IRTemplate) -> str:
    """Generate resources.py with Resources and PropertyType wrappers (single file mode)."""
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
        lines.append(f"from .stack_config import {', '.join(sorted_refs)}")

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


def _logical_id_to_filename(logical_id: str) -> str:
    """Convert LogicalId to snake_case filename (without .py extension)."""
    from cloudformation_dataclasses.importer.parser import to_snake_case
    return to_snake_case(logical_id)


def _find_resource_dependencies(
    template: IRTemplate,
    resource_id: str,
    name_pattern_map: dict[str, str] | None = None,
    arn_pattern_map: dict[str, tuple[str, str]] | None = None,
) -> set[str]:
    """Find other resources that this resource depends on (for imports).

    Args:
        template: The IR template
        resource_id: The resource we're finding dependencies for
        name_pattern_map: Map of Sub patterns to resource IDs for implicit ref detection
        arn_pattern_map: Map of ARN Sub patterns to (resource_id, suffix) for get_att detection
    """
    deps = set()

    # Explicit references from reference graph
    for ref_target in template.reference_graph.get(resource_id, []):
        if ref_target in template.resources and ref_target != resource_id:
            deps.add(ref_target)

    # Implicit references from Sub patterns that match resource names or ARNs
    resource = template.resources.get(resource_id)
    if resource:
        _find_sub_pattern_refs(
            resource.properties, name_pattern_map, arn_pattern_map, resource_id, deps, template
        )

        # DependsOn references (for class-based depends_on)
        for dep in resource.depends_on:
            if dep in template.resources and dep != resource_id:
                deps.add(dep)

    return deps


def _find_sub_pattern_refs(
    properties: dict[str, Any],
    name_pattern_map: dict[str, str] | None,
    arn_pattern_map: dict[str, tuple[str, str]] | None,
    current_resource_id: str,
    deps: set[str],
    template: IRTemplate,
) -> None:
    """Recursively find Sub patterns that reference other resources."""
    for prop in properties.values():
        if hasattr(prop, 'value'):
            _find_sub_in_value(
                prop.value, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
            )


def _find_sub_in_value(
    value: Any,
    name_pattern_map: dict[str, str] | None,
    arn_pattern_map: dict[str, tuple[str, str]] | None,
    current_resource_id: str,
    deps: set[str],
    template: IRTemplate,
) -> None:
    """Recursively find Sub patterns in a value."""
    if isinstance(value, IRIntrinsic):
        if value.type == IntrinsicType.SUB:
            # Extract template string
            if isinstance(value.args, str):
                template_str = value.args
            elif isinstance(value.args, (list, tuple)) and len(value.args) >= 1:
                template_str = value.args[0]
            else:
                template_str = None

            if template_str:
                # Extract variable references from the template string
                var_refs = re.findall(r"\$\{([^}]+)\}", template_str)
                # Filter out pseudo-parameters (AWS::*)
                non_pseudo_vars = [v for v in var_refs if not v.startswith("AWS::")]
                # Check if all non-pseudo vars are parameters
                all_params = all(v in template.parameters for v in non_pseudo_vars)

                # Check if it matches a resource name pattern (ref dependency)
                # This creates a dependency because the generated code uses ref(ResourceName)
                if name_pattern_map and template_str in name_pattern_map:
                    ref_target = name_pattern_map[template_str]
                    if ref_target != current_resource_id:
                        deps.add(ref_target)
                # Check if it matches an ARN pattern (get_att dependency)
                # Only add dependency if we would actually convert to get_att()
                # Skip if all non-pseudo vars are parameters (we keep Sub in that case)
                elif arn_pattern_map and template_str in arn_pattern_map:
                    if not all_params:
                        ref_target, _ = arn_pattern_map[template_str]
                        if ref_target != current_resource_id:
                            deps.add(ref_target)

        # Also check nested intrinsics
        if isinstance(value.args, (list, tuple)):
            for arg in value.args:
                _find_sub_in_value(
                    arg, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
                )
        elif isinstance(value.args, dict):
            for v in value.args.values():
                _find_sub_in_value(
                    v, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
                )
    elif isinstance(value, dict):
        for v in value.values():
            _find_sub_in_value(
                v, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
            )
    elif isinstance(value, list):
        for item in value:
            _find_sub_in_value(
                item, name_pattern_map, arn_pattern_map, current_resource_id, deps, template
            )


def _generate_stack_package(pkg_ctx: PackageContext, template: IRTemplate) -> dict[str, str]:
    """Generate stack/ directory with params, outputs, and consolidated resources.

    Resources are consolidated into fewer files:
    - If total resources < 5: all go in main.py
    - SCCs (cyclic dependencies) always go in main.py
    - Single-resource groups also go in main.py
    - Only large templates with multiple non-SCC resources get separate files

    Returns:
        Dict mapping "stack/<filename>.py" to content
    """
    files = {}
    ctx = pkg_ctx.codegen_ctx

    # Find strongly connected components to detect cycles
    sccs = _find_strongly_connected_components(template)

    # Map each resource to its SCC (for grouping)
    resource_to_scc: dict[str, int] = {}
    for scc_idx, scc in enumerate(sccs):
        for resource_id in scc:
            resource_to_scc[resource_id] = scc_idx

    # Build SCC ordering info for forward reference detection
    scc_orderings: dict[int, list[str]] = {}  # scc_idx -> ordered list of resource IDs
    for scc_idx, scc in enumerate(sccs):
        if len(scc) > 1:
            scc_orderings[scc_idx] = _order_scc_resources(scc, template)

    # First pass: generate all resources and collect their PropertyType classes
    # For SCC members, set up forward_references before generating
    sorted_resources = _topological_sort(template)
    resource_classes: dict[str, tuple[str, list[str]]] = {}  # id -> (class_def, [pt_defs])

    for resource_id in sorted_resources:
        resource = template.resources[resource_id]
        ctx.property_type_class_defs = []

        # Set up forward references for SCC members
        scc_idx = resource_to_scc[resource_id]
        if scc_idx in scc_orderings:
            ordered_scc = scc_orderings[scc_idx]
            # Resources after this one in the ordering are forward references
            resource_pos = ordered_scc.index(resource_id)
            ctx.forward_references = set(ordered_scc[resource_pos + 1:])
        else:
            ctx.forward_references = set()

        resource_class = _generate_resource_class(resource, ctx)
        resource_classes[resource_id] = (resource_class, list(ctx.property_type_class_defs))
        pkg_ctx.resources_exports.add(resource_id)

    # Clear forward_references after generation
    ctx.forward_references = set()

    # Second pass: decide which resources go to main.py vs separate files
    # Collect resources for main.py and track separate files
    main_py_resources: list[str] = []  # ordered list of resource IDs for main.py
    separate_files: dict[str, list[str]] = {}  # filename -> ordered resource IDs
    generated_sccs: set[int] = set()

    for resource_id in sorted_resources:
        scc_idx = resource_to_scc[resource_id]
        if scc_idx in generated_sccs:
            continue
        generated_sccs.add(scc_idx)

        scc = sccs[scc_idx]

        if len(scc) > 1:
            # SCC (cyclic dependencies) goes to main.py
            main_py_resources.extend(scc_orderings[scc_idx])
        else:
            # Single resource: group by category
            resource = template.resources[resource_id]
            category = _get_resource_category(resource)
            if category == "main":
                main_py_resources.append(resource_id)
            else:
                if category not in separate_files:
                    separate_files[category] = []
                separate_files[category].append(resource_id)

    # Build file-level dependency graph and move resources to break import cycles
    # This is necessary because category files are loaded dynamically by setup_resources()
    # which uses topological sort - if there's a cycle, it can't resolve correctly.
    #
    # Example cycle: compute.py (EC2) -> network.py (SecurityGroup) -> main.py (CustomResource) -> compute.py
    # Fix: move resources from category files to main.py until no cycles remain
    resource_to_file: dict[str, str] = {}
    for rid in main_py_resources:
        resource_to_file[rid] = "main"
    for cat, rids in separate_files.items():
        for rid in rids:
            resource_to_file[rid] = cat

    # Build resource dependency map (resource_id -> set of resource_ids it depends on)
    # Use only explicit references (reference_graph + DependsOn), not Sub pattern matching
    all_resource_deps: dict[str, set[str]] = {}
    for rid in template.resources:
        all_resource_deps[rid] = _find_resource_dependencies(template, rid)

    # Iteratively move resources to main.py to break file-level cycles
    max_iterations = len(template.resources) + 1
    for _ in range(max_iterations):
        # Build file-level dependency graph
        file_deps: dict[str, set[str]] = {"main": set()}
        for cat in separate_files:
            file_deps[cat] = set()

        for rid, rid_deps in all_resource_deps.items():
            rid_file = resource_to_file.get(rid, "main")
            for dep_rid in rid_deps:
                dep_file = resource_to_file.get(dep_rid, "main")
                if dep_file != rid_file:
                    file_deps[rid_file].add(dep_file)

        # Detect cycles using DFS
        def find_cycle() -> list[str] | None:
            visited: set[str] = set()
            rec_stack: set[str] = set()
            path: list[str] = []

            def dfs(node: str) -> list[str] | None:
                visited.add(node)
                rec_stack.add(node)
                path.append(node)

                for neighbor in file_deps.get(node, set()):
                    if neighbor not in visited:
                        result = dfs(neighbor)
                        if result:
                            return result
                    elif neighbor in rec_stack:
                        # Found cycle - return the cycle path
                        cycle_start = path.index(neighbor)
                        return path[cycle_start:]

                path.pop()
                rec_stack.remove(node)
                return None

            for node in file_deps:
                if node not in visited:
                    result = dfs(node)
                    if result:
                        return result
            return None

        cycle = find_cycle()
        if not cycle:
            break  # No cycles, we're done

        # Move all resources from non-main cycle members to main.py
        for cycle_file in cycle:
            if cycle_file != "main" and cycle_file in separate_files:
                # Move all resources from this category to main
                for rid in separate_files[cycle_file]:
                    main_py_resources.append(rid)
                    resource_to_file[rid] = "main"
                del separate_files[cycle_file]

    # Re-sort resources in topological order to ensure dependencies come first
    topo_order = {rid: idx for idx, rid in enumerate(sorted_resources)}
    main_py_resources.sort(key=lambda rid: topo_order[rid])
    for category in separate_files:
        separate_files[category].sort(key=lambda rid: topo_order[rid])

    # Generate main.py with all consolidated resources
    if main_py_resources:
        lines = []
        lines.append('"""Stack resources."""')
        lines.append("")
        lines.append("from .. import *  # noqa: F403")
        lines.append("")
        lines.append("")

        for res_id in main_py_resources:
            resource_class, pt_defs = resource_classes[res_id]

            # PropertyType wrappers for this resource
            for pt_def in pt_defs:
                lines.append(pt_def)
                lines.append("")
                lines.append("")

            # The resource class itself
            lines.append(resource_class)
            lines.append("")
            lines.append("")

        # Remove trailing empty lines
        while lines and lines[-1] == "":
            lines.pop()

        files["stack/main.py"] = "\n".join(lines) + "\n"

    # Generate category files (compute.py, network.py, etc.)
    for filename, resource_ids in separate_files.items():
        lines = []
        resource_names = ", ".join(resource_ids)
        lines.append(f'"""{filename.title()} resources: {resource_names}."""')
        lines.append("")
        lines.append("from .. import *  # noqa: F403")
        lines.append("")
        lines.append("")

        for res_id in resource_ids:
            resource_class, pt_defs = resource_classes[res_id]

            for pt_def in pt_defs:
                lines.append(pt_def)
                lines.append("")
                lines.append("")

            lines.append(resource_class)
            lines.append("")
            lines.append("")

        while lines and lines[-1] == "":
            lines.pop()

        files[f"stack/{filename}.py"] = "\n".join(lines) + "\n"

    # Generate stack/__init__.py that re-exports params, outputs, and resources
    init_lines = ['"""Stack - parameters, outputs, and resources."""']
    init_lines.append("from .params import *  # noqa: F403, F401")
    init_lines.append("")
    init_lines.append("# Import resources with topological ordering")
    init_lines.append("from cloudformation_dataclasses.core.resource_loader import setup_resources")
    init_lines.append('setup_resources(__file__, __name__, globals())')
    init_lines.append("")
    init_lines.append("# Import outputs after resources (outputs reference resource classes)")
    init_lines.append("try:")
    init_lines.append("    from .outputs import *  # noqa: F403, F401")
    init_lines.append("except ImportError:")
    init_lines.append("    pass")
    init_lines.append("")
    files["stack/__init__.py"] = "\n".join(init_lines)

    return files


def _order_scc_resources(
    scc: list[str],
    template: IRTemplate,
    name_pattern_map: dict[str, str] | None = None,
    arn_pattern_map: dict[str, tuple[str, str]] | None = None,
) -> list[str]:
    """Order resources within an SCC to minimize forward references.

    Uses a heuristic: resources with fewer dependencies on other SCC members
    come first.
    """
    scc_set = set(scc)

    # Build pattern maps if not provided
    if name_pattern_map is None:
        name_pattern_map = _build_name_pattern_map(template)
    if arn_pattern_map is None:
        arn_pattern_map = _build_arn_pattern_map(template)

    # Count how many SCC members each resource depends on
    # Use full dependency detection (including implicit refs from code generation)
    dep_counts: dict[str, int] = {}
    for resource_id in scc:
        deps = _find_resource_dependencies(
            template, resource_id, name_pattern_map, arn_pattern_map
        )
        scc_deps = [d for d in deps if d in scc_set]
        dep_counts[resource_id] = len(scc_deps)

    # Sort by dependency count (ascending), then alphabetically for stability
    return sorted(scc, key=lambda r: (dep_counts[r], r))


def _generate_outputs_py(pkg_ctx: PackageContext, template: IRTemplate) -> str | None:
    """Generate stack/outputs.py with Output definitions.

    Returns None if there are no outputs to generate.
    """
    if not template.outputs:
        return None

    lines = []
    lines.append('"""Template outputs."""')
    lines.append("")
    lines.append("from .. import *  # noqa: F403")
    lines.append("")
    lines.append("")

    ctx = pkg_ctx.codegen_ctx

    # Outputs
    for output in template.outputs.values():
        class_def = _generate_output_class(output, ctx)
        lines.append(class_def)
        lines.append("")
        lines.append("")
        pkg_ctx.outputs_exports.add(f"{output.logical_id}Output")

    # Remove trailing empty lines
    while lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines) + "\n"


def _generate_main_py(pkg_ctx: PackageContext, template: IRTemplate) -> str:
    """Generate main.py with build_template and __main__."""
    lines = []
    lines.append('"""Template builder."""')
    lines.append("")
    # Import from parent package (gets Template + all stack re-exports)
    lines.append("from . import *  # noqa: F403, F401")
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
    lines.append("def main() -> None:")
    lines.append('    """Print the CloudFormation template as JSON."""')
    lines.append("    import json")
    lines.append("    template = build_template()")
    lines.append("    print(json.dumps(template.to_dict(), indent=2))")
    lines.append("")
    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append("    main()")

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


def _detect_aws_name_collisions(ctx: CodegenContext, template: IRTemplate) -> None:
    """
    Pre-scan template to detect AWS class names that appear in multiple modules.

    When multiple resources use the same class name from different modules
    (e.g., iam.Policy and iot.Policy), we need to use qualified imports
    to avoid Python import collisions.

    Populates ctx.colliding_aws_names with name -> module mapping.
    """
    # Track all AWS class names and their modules
    aws_class_to_modules: dict[str, set[str]] = {}

    for resource in template.resources.values():
        resolved = resolve_resource_type(resource.resource_type)
        if resolved:
            module, class_name = resolved
            aws_class_to_modules.setdefault(class_name, set()).add(module)

    # Find colliding names (same class name in multiple modules)
    for class_name, modules in aws_class_to_modules.items():
        if len(modules) > 1:
            # This name appears in multiple modules - mark as colliding
            # Store each module for the colliding name
            for module in modules:
                ctx.colliding_aws_names[class_name] = module  # Last one stored


def generate_package(template: IRTemplate, package_name: str) -> dict[str, str]:
    """
    Generate a Python package from template (multi-file output).

    Args:
        template: Parsed IRTemplate
        package_name: Name of the Python package (used as subdirectory prefix)

    Returns:
        Dict mapping filename to content, with all files prefixed by package_name/:
        - "{package_name}/__init__.py": Centralized imports (re-exports from .stack)
        - "{package_name}/main.py": build_template + entry point
        - "{package_name}/__main__.py": Entry point for python -m
        - "{package_name}/stack/": Directory with params, outputs, and resources
    """
    pkg_ctx = PackageContext(template=template)

    # Initialize codegen context
    ctx = pkg_ctx.codegen_ctx
    ctx.add_import("cloudformation_dataclasses.core", "ref")
    ctx.add_import("cloudformation_dataclasses.core", "get_att")
    ctx.add_import("cloudformation_dataclasses.core", "Template")

    # Pre-pass: detect AWS class name collisions across modules
    # We need to know this before generating resource files so they can use qualified names
    _detect_aws_name_collisions(ctx, template)

    # Generate stack/params.py (Parameters, Mappings, Conditions)
    params_content = _generate_params_py(pkg_ctx, template)

    # Generate stack/outputs.py (if there are outputs)
    outputs_content = _generate_outputs_py(pkg_ctx, template)

    # Generate stack/ package (consolidated resources + __init__.py)
    stack_files = _generate_stack_package(pkg_ctx, template)

    # Generate main.py (build_template)
    main_content = _generate_main_py(pkg_ctx, template)

    # Generate __init__.py last (after all imports collected)
    init_content = _generate_init_py(pkg_ctx, template)

    # Generate __main__.py for `python -m package_name` support
    dunder_main_content = f'''"""Allow running as: python -m {package_name}."""
from .main import main

main()
'''

    # Prefix all files with package_name/ for nested package structure
    files = {
        f"{package_name}/__init__.py": init_content,
        f"{package_name}/__main__.py": dunder_main_content,
        f"{package_name}/main.py": main_content,
        f"{package_name}/stack/params.py": params_content,
    }

    # Add stack/outputs.py if there are outputs
    if outputs_content:
        files[f"{package_name}/stack/outputs.py"] = outputs_content

    # Add all stack files (already have stack/ prefix, add package_name/)
    for filename, content in stack_files.items():
        files[f"{package_name}/{filename}"] = content

    return files


