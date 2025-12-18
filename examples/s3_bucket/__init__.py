"""S3 bucket example - exports for cleaner imports."""

from cloudformation_dataclasses.aws.s3 import (
    Bucket,
    BucketEncryption,
    BucketPolicy,
    BucketVersioningStatus,
    ServerSideEncryptionByDefault,
    ServerSideEncryptionRule,
    VersioningConfiguration,
)
from cloudformation_dataclasses.core import (
    DenyStatement,
    DeploymentContext,
    PolicyDocument,
    Tag,
    Template,
    cloudformation_dataclass,
    ref,
)
from cloudformation_dataclasses.intrinsics import Sub

__all__ = [
    "Bucket",
    "BucketEncryption",
    "BucketPolicy",
    "BucketVersioningStatus",
    "ServerSideEncryptionByDefault",
    "ServerSideEncryptionRule",
    "VersioningConfiguration",
    "DenyStatement",
    "DeploymentContext",
    "PolicyDocument",
    "Tag",
    "Template",
    "cloudformation_dataclass",
    "ref",
    "Sub",
]
