"""S3 CloudFormation template examples."""

from cloudformation_dataclasses.aws.s3 import (
    # Resources
    Bucket,
    BucketPolicy,
    # Property types
    BucketEncryption,
    PublicAccessBlockConfiguration,
    ServerSideEncryptionByDefault,
    ServerSideEncryptionRule,
    VersioningConfiguration,
    # Enum constants
    BucketVersioningStatus,
    ServerSideEncryption,
)
from cloudformation_dataclasses.core import (
    # Parameter types
    STRING,
    # Core constructs
    DenyStatement,
    DeploymentContext,
    Output,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    Tag,
    Template,
    cloudformation_dataclass,
    ref,
)
from cloudformation_dataclasses.intrinsics import (
    Join,
    Sub,
    AWS_PARTITION,
)

__all__ = [
    # Resources
    "Bucket",
    "BucketPolicy",
    # Property types
    "BucketEncryption",
    "PublicAccessBlockConfiguration",
    "ServerSideEncryptionByDefault",
    "ServerSideEncryptionRule",
    "VersioningConfiguration",
    # Enum constants
    "BucketVersioningStatus",
    "ServerSideEncryption",
    # Core
    "DenyStatement",
    "DeploymentContext",
    "Output",
    "Parameter",
    "PolicyDocument",
    "PolicyStatement",
    "STRING",
    "Tag",
    "Template",
    "cloudformation_dataclass",
    "ref",
    # Intrinsics
    "Join",
    "Sub",
    "AWS_PARTITION",
]
