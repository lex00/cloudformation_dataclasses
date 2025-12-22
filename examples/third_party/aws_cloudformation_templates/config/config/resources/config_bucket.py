from __future__ import annotations

"""ConfigBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ConfigBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ConfigBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = ConfigBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ConfigBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [ConfigBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ConfigBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ConfigBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = ConfigBucketBucketEncryption
    public_access_block_configuration = ConfigBucketPublicAccessBlockConfiguration
