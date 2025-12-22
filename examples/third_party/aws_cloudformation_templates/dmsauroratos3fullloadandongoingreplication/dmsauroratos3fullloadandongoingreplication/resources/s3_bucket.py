"""S3Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class S3BucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class S3BucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [S3BucketServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = S3BucketBucketEncryption
    public_access_block_configuration = S3BucketPublicAccessBlockConfiguration
