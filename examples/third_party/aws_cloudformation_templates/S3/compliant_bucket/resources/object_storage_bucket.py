"""ObjectStorageBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ObjectStorageBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ObjectStorageBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = ObjectStorageBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ObjectStorageBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [ObjectStorageBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ObjectStorageBucketLoggingConfiguration:
    resource: LoggingConfiguration
    destination_bucket_name = ref("ObjectStorageLogBucket")


@cloudformation_dataclass
class ObjectStorageBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ObjectStorageBucketReplicationDestination:
    resource: ReplicationDestination
    bucket = get_att("ObjectStorageReplicaBucket", ARN)


@cloudformation_dataclass
class ObjectStorageBucketReplicationRule:
    resource: ReplicationRule
    destination = ObjectStorageBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class ObjectStorageBucketReplicationConfiguration:
    resource: ReplicationConfiguration
    role = get_att("ObjectStorageReplicationRole", ARN)
    rules = [ObjectStorageBucketReplicationRule]


@cloudformation_dataclass
class ObjectStorageBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ObjectStorageBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = ObjectStorageBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ObjectStorageBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ObjectStorageBucketPublicAccessBlockConfiguration
    replication_configuration = ObjectStorageBucketReplicationConfiguration
    versioning_configuration = ObjectStorageBucketVersioningConfiguration
