"""SiteContentLogBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteContentLogBucketServerSideEncryptionByDefault:
    resource: s3.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteContentLogBucketServerSideEncryptionRule:
    resource: s3.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteContentLogBucketBucketEncryption:
    resource: s3.BucketEncryption
    server_side_encryption_configuration = [SiteContentLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteContentLogBucketDefaultRetention:
    resource: DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class SiteContentLogBucketObjectLockRule:
    resource: ObjectLockRule
    default_retention = SiteContentLogBucketDefaultRetention


@cloudformation_dataclass
class SiteContentLogBucketObjectLockConfiguration:
    resource: ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = SiteContentLogBucketObjectLockRule


@cloudformation_dataclass
class SiteContentLogBucketPublicAccessBlockConfiguration:
    resource: s3.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteContentLogBucketVersioningConfiguration:
    resource: s3.VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteContentLogBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = SiteContentLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = SiteContentLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = SiteContentLogBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteContentLogBucketVersioningConfiguration
