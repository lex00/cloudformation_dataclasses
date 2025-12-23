"""StorageBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StorageBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class StorageBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = StorageBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class StorageBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [StorageBucketServerSideEncryptionRule]


@cloudformation_dataclass
class StorageBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(StorageLogBucket)


@cloudformation_dataclass
class StorageBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class StorageBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(StorageReplicaBucket, "Arn")


@cloudformation_dataclass
class StorageBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = StorageBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class StorageBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(StorageReplicationRole, "Arn")
    rules = [StorageBucketReplicationRule]


@cloudformation_dataclass
class StorageBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class StorageBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = StorageBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = StorageBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = StorageBucketPublicAccessBlockConfiguration
    replication_configuration = StorageBucketReplicationConfiguration
    versioning_configuration = StorageBucketDeleteMarkerReplication
