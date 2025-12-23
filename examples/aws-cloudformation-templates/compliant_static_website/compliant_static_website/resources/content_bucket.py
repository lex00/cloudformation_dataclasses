"""ContentBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ContentBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ContentBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = ContentBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ContentBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [ContentBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ContentBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(ContentLogBucket)


@cloudformation_dataclass
class ContentBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ContentBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(ContentReplicaBucket, "Arn")


@cloudformation_dataclass
class ContentBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = ContentBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class ContentBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(ContentReplicationRole, "Arn")
    rules = [ContentBucketReplicationRule]


@cloudformation_dataclass
class ContentBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class ContentBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = ContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ContentBucketPublicAccessBlockConfiguration
    replication_configuration = ContentBucketReplicationConfiguration
    versioning_configuration = ContentBucketDeleteMarkerReplication
