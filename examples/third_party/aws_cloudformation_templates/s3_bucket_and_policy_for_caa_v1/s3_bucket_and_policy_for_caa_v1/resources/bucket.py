"""Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class BucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class BucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [BucketServerSideEncryptionRule]


@cloudformation_dataclass
class BucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class BucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = ref(BucketName)
    bucket_encryption = BucketBucketEncryption
    versioning_configuration = BucketVersioningConfiguration
    public_access_block_configuration = BucketPublicAccessBlockConfiguration
