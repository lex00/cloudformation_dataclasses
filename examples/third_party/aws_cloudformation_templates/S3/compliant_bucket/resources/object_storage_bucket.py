from __future__ import annotations

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
class ObjectStorageBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ObjectStorageBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    restrict_public_buckets = True
    block_public_policy = True
    block_public_acls = True
    ignore_public_acls = True


@cloudformation_dataclass
class ObjectStorageBucketLoggingConfiguration:
    resource: LoggingConfiguration
    destination_bucket_name: Ref[ObjectStorageLogBucket] = ref()


@cloudformation_dataclass
class ObjectStorageBucketReplicationDestination:
    resource: ReplicationDestination
    bucket: GetAtt[ObjectStorageReplicaBucket] = get_att("Arn")


@cloudformation_dataclass
class ObjectStorageBucketReplicationRule:
    resource: ReplicationRule
    status = ReplicationRuleStatus.ENABLED
    destination = ObjectStorageBucketReplicationDestination


@cloudformation_dataclass
class ObjectStorageBucketReplicationConfiguration:
    resource: ReplicationConfiguration
    role: GetAtt[ObjectStorageReplicationRole] = get_att("Arn")
    rules = [ObjectStorageBucketReplicationRule]


@cloudformation_dataclass
class ObjectStorageBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = ObjectStorageBucketBucketEncryption
    versioning_configuration = ObjectStorageBucketVersioningConfiguration
    public_access_block_configuration = ObjectStorageBucketPublicAccessBlockConfiguration
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    object_lock_enabled = False
    logging_configuration = ObjectStorageBucketLoggingConfiguration
    replication_configuration = ObjectStorageBucketReplicationConfiguration
    tags = []
