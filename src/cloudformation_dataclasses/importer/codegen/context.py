"""Code generation context classes."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Optional

from cloudformation_dataclasses.importer.ir import (
    IntrinsicType,
    IRIntrinsic,
    IRTemplate,
)


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


# =============================================================================
# Package Context
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
            self.codegen_ctx.name_pattern_map = build_name_pattern_map(self.template)
            self.codegen_ctx.arn_pattern_map = build_arn_pattern_map(self.template)


# =============================================================================
# Reuse Analysis
# =============================================================================


def analyze_reuse(template: IRTemplate) -> dict[str, int]:
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


# =============================================================================
# Pattern Map Building (for implicit ref/get_att detection)
# =============================================================================


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


def build_name_pattern_map(template: IRTemplate) -> dict[str, str]:
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


def build_arn_pattern_map(template: IRTemplate) -> dict[str, tuple[str, str]]:
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
