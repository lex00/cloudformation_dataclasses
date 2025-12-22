"""S3Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketServerSideEncryptionByDefault:
    resource: s3.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class S3BucketServerSideEncryptionRule:
    resource: s3.ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class S3BucketBucketEncryption:
    resource: s3.BucketEncryption
    server_side_encryption_configuration = [S3BucketServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketPublicAccessBlockConfiguration:
    resource: s3.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = S3BucketBucketEncryption
    public_access_block_configuration = S3BucketPublicAccessBlockConfiguration
