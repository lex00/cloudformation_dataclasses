"""SiteCloudFrontLogsBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: s3.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteCloudFrontLogsBucketServerSideEncryptionRule:
    resource: s3.ServerSideEncryptionRule
    server_side_encryption_by_default = SiteCloudFrontLogsBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteCloudFrontLogsBucketBucketEncryption:
    resource: s3.BucketEncryption
    server_side_encryption_configuration = [SiteCloudFrontLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketLoggingConfiguration:
    resource: s3.LoggingConfiguration
    destination_bucket_name = ref(SiteCloudFrontLogsLogBucket)


@cloudformation_dataclass
class SiteCloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: s3.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationDestination:
    resource: s3.ReplicationDestination
    bucket = get_att(SiteCloudFrontLogsReplicaBucket, "Arn")


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationRule:
    resource: s3.ReplicationRule
    destination = SiteCloudFrontLogsBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class SiteCloudFrontLogsBucketReplicationConfiguration:
    resource: s3.ReplicationConfiguration
    role = get_att(SiteCloudFrontLogsReplicationRole, "Arn")
    rules = [SiteCloudFrontLogsBucketReplicationRule]


@cloudformation_dataclass
class SiteCloudFrontLogsBucketVersioningConfiguration:
    resource: s3.VersioningConfiguration
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

    resource: s3.Bucket
    bucket_encryption = SiteCloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteCloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteCloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = SiteCloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = SiteCloudFrontLogsBucketVersioningConfiguration
    ownership_controls = SiteCloudFrontLogsBucketOwnershipControls
