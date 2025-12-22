"""Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class BucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = BucketServerSideEncryptionByDefault


@cloudformation_dataclass
class BucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [BucketServerSideEncryptionRule]


@cloudformation_dataclass
class BucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class BucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
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
    versioning_configuration = BucketDeleteMarkerReplication
    public_access_block_configuration = BucketPublicAccessBlockConfiguration
