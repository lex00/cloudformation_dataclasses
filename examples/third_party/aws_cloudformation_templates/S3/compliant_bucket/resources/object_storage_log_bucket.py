"""ObjectStorageLogBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ObjectStorageLogBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ObjectStorageLogBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = ObjectStorageLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ObjectStorageLogBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [ObjectStorageLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ObjectStorageLogBucketDefaultRetention:
    resource: DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class ObjectStorageLogBucketObjectLockRule:
    resource: ObjectLockRule
    default_retention = ObjectStorageLogBucketDefaultRetention


@cloudformation_dataclass
class ObjectStorageLogBucketObjectLockConfiguration:
    resource: ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = ObjectStorageLogBucketObjectLockRule


@cloudformation_dataclass
class ObjectStorageLogBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ObjectStorageLogBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ObjectStorageLogBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = ObjectStorageLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = ObjectStorageLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = ObjectStorageLogBucketPublicAccessBlockConfiguration
    versioning_configuration = ObjectStorageLogBucketVersioningConfiguration
