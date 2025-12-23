"""ObjectStorageBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ObjectStorageBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ObjectStorageBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ObjectStorageBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ObjectStorageBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ObjectStorageBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ObjectStorageBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(ObjectStorageLogBucket)


@cloudformation_dataclass
class ObjectStorageBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ObjectStorageBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(ObjectStorageReplicaBucket, "Arn")


@cloudformation_dataclass
class ObjectStorageBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = ObjectStorageBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class ObjectStorageBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(ObjectStorageReplicationRole, "Arn")
    rules = [ObjectStorageBucketReplicationRule]


@cloudformation_dataclass
class ObjectStorageBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class ObjectStorageBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ObjectStorageBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ObjectStorageBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ObjectStorageBucketPublicAccessBlockConfiguration
    replication_configuration = ObjectStorageBucketReplicationConfiguration
    versioning_configuration = ObjectStorageBucketDeleteMarkerReplication
