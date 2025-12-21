from __future__ import annotations

"""StorageBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StorageBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class StorageBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = StorageBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class StorageBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [StorageBucketServerSideEncryptionRule]


@cloudformation_dataclass
class StorageBucketLoggingConfiguration:
    resource: LoggingConfiguration
    destination_bucket_name: Ref[StorageLogBucket] = ref()


@cloudformation_dataclass
class StorageBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class StorageBucketReplicationDestination:
    resource: ReplicationDestination
    bucket: GetAtt[StorageReplicaBucket] = get_att("Arn")


@cloudformation_dataclass
class StorageBucketReplicationRule:
    resource: ReplicationRule
    destination = StorageBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class StorageBucketReplicationConfiguration:
    resource: ReplicationConfiguration
    role: GetAtt[StorageReplicationRole] = get_att("Arn")
    rules = [StorageBucketReplicationRule]


@cloudformation_dataclass
class StorageBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class StorageBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = StorageBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = StorageBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = StorageBucketPublicAccessBlockConfiguration
    replication_configuration = StorageBucketReplicationConfiguration
    versioning_configuration = StorageBucketVersioningConfiguration
