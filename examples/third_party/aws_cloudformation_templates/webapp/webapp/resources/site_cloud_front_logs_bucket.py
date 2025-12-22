from __future__ import annotations

"""SiteCloudFrontLogsBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketLoggingConfiguration:
    resource: LoggingConfiguration
    destination_bucket_name: Ref[SiteCloudFrontLogsLogBucket] = ref()


@cloudformation_dataclass
class SiteCloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationDestination:
    resource: ReplicationDestination
    bucket: GetAtt[SiteCloudFrontLogsReplicaBucket] = get_att("Arn")


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationRule:
    resource: ReplicationRule
    destination = SiteCloudFrontLogsBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationConfiguration:
    resource: ReplicationConfiguration
    role: GetAtt[SiteCloudFrontLogsReplicationRole] = get_att("Arn")
    rules = [SiteCloudFrontLogsBucketReplicationRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsBucketOwnershipControlsRule:
    resource: OwnershipControlsRule
    object_ownership = 'BucketOwnerPreferred'


@cloudformation_dataclass
class SiteCloudFrontLogsBucketOwnershipControls:
    resource: OwnershipControls
    rules = [SiteCloudFrontLogsBucketOwnershipControlsRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = SiteCloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteCloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = SiteCloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = SiteCloudFrontLogsBucketVersioningConfiguration
    ownership_controls = SiteCloudFrontLogsBucketOwnershipControls
