"""StorageLogBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StorageLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class StorageLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = StorageLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class StorageLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [StorageLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class StorageLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class StorageLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = StorageLogBucketDefaultRetention


@cloudformation_dataclass
class StorageLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = StorageLogBucketObjectLockRule


@cloudformation_dataclass
class StorageLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class StorageLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class StorageLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = StorageLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = StorageLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = StorageLogBucketPublicAccessBlockConfiguration
    versioning_configuration = StorageLogBucketDeleteMarkerReplication
