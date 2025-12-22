"""ContentLogBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ContentLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ContentLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ContentLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ContentLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ContentLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class ContentLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = ContentLogBucketDefaultRetention


@cloudformation_dataclass
class ContentLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = ContentLogBucketObjectLockRule


@cloudformation_dataclass
class ContentLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ContentLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class ContentLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = ContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = ContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = ContentLogBucketDeleteMarkerReplication
