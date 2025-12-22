"""SiteCloudFrontLogsReplicaBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsReplicaBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = SiteCloudFrontLogsReplicaBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
    versioning_configuration = SiteCloudFrontLogsReplicaBucketVersioningConfiguration
