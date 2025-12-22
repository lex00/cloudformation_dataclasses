"""SiteContentBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteContentBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class SiteContentBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = SiteContentBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class SiteContentBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [SiteContentBucketServerSideEncryptionRule]


@cloudformation_dataclass
class SiteContentBucketLoggingConfiguration:
    resource: LoggingConfiguration
    destination_bucket_name = ref(SiteContentLogBucket)


@cloudformation_dataclass
class SiteContentBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class SiteContentBucketReplicationDestination:
    resource: ReplicationDestination
    bucket = get_att(SiteContentReplicaBucket, "Arn")


@cloudformation_dataclass
class SiteContentBucketReplicationRule:
    resource: ReplicationRule
    destination = SiteContentBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class SiteContentBucketReplicationConfiguration:
    resource: ReplicationConfiguration
    role = get_att(SiteContentReplicationRole, "Arn")
    rules = [SiteContentBucketReplicationRule]


@cloudformation_dataclass
class SiteContentBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class SiteContentBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = SiteContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-content-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = SiteContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = SiteContentBucketPublicAccessBlockConfiguration
    replication_configuration = SiteContentBucketReplicationConfiguration
    versioning_configuration = SiteContentBucketVersioningConfiguration
