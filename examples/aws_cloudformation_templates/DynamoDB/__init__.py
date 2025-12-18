"""DynamoDB CloudFormation template examples."""

from cloudformation_dataclasses.aws.dynamodb import (
    # Resources and property types
    AttributeDefinition,
    GlobalSecondaryIndex,
    KeySchema,
    LocalSecondaryIndex,
    PointInTimeRecoverySpecification,
    Projection,
    ProvisionedThroughput,
    Table,
    # DynamoDB-specific constants (auto-generated from botocore)
    HASH,
    RANGE,
    KeyType,
    S,
    AttributeType,
    KEYS_ONLY,
    ProjectionType,
)
from cloudformation_dataclasses.core import (
    # Parameter types
    NUMBER,
    STRING,
    ParameterType,
    # Core constructs
    DeploymentContext,
    Output,
    Parameter,
    Tag,
    Template,
    cloudformation_dataclass,
    ref,
)

__all__ = [
    "AttributeDefinition",
    "AttributeType",
    "DeploymentContext",
    "GlobalSecondaryIndex",
    "HASH",
    "KEYS_ONLY",
    "KeySchema",
    "KeyType",
    "LocalSecondaryIndex",
    "NUMBER",
    "Output",
    "Parameter",
    "ParameterType",
    "PointInTimeRecoverySpecification",
    "Projection",
    "ProjectionType",
    "ProvisionedThroughput",
    "RANGE",
    "S",
    "STRING",
    "Table",
    "Tag",
    "Template",
    "cloudformation_dataclass",
    "ref",
]
