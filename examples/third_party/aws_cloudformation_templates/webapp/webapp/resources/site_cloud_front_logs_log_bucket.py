"""SiteCloudFrontLogsLogBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketDefaultRetention:
    resource: s3.bucket.DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketObjectLockRule:
    resource: s3.bucket.ObjectLockRule
    default_retention = SiteCloudFrontLogsLogBucketDefaultRetention


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketObjectLockConfiguration:
    resource: s3.bucket.ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = SiteCloudFrontLogsLogBucketObjectLockRule


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class SiteCloudFrontLogsLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteCloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsLogBucketDeleteMarkerReplication
