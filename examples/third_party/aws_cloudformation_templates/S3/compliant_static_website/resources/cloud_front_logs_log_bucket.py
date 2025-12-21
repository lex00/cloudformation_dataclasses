from __future__ import annotations

"""CloudFrontLogsLogBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontLogsLogBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class CloudFrontLogsLogBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsLogBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class CloudFrontLogsLogBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsLogBucketServerSideEncryptionRule]


@cloudformation_dataclass
class CloudFrontLogsLogBucketDefaultRetention:
    resource: DefaultRetention
    mode = ObjectLockRetentionMode.COMPLIANCE
    years = 1


@cloudformation_dataclass
class CloudFrontLogsLogBucketObjectLockRule:
    resource: ObjectLockRule
    default_retention = CloudFrontLogsLogBucketDefaultRetention


@cloudformation_dataclass
class CloudFrontLogsLogBucketObjectLockConfiguration:
    resource: ObjectLockConfiguration
    object_lock_enabled = ObjectLockEnabled.ENABLED
    rule = CloudFrontLogsLogBucketObjectLockRule


@cloudformation_dataclass
class CloudFrontLogsLogBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class CloudFrontLogsLogBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsLogBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = CloudFrontLogsLogBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-logs-${AWS::Region}-${AWS::AccountId}')
    object_lock_configuration = CloudFrontLogsLogBucketObjectLockConfiguration
    object_lock_enabled = True
    public_access_block_configuration = CloudFrontLogsLogBucketPublicAccessBlockConfiguration
    versioning_configuration = CloudFrontLogsLogBucketVersioningConfiguration
