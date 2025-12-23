"""CloudFrontLogsBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class CloudFrontLogsBucketServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class CloudFrontLogsBucketBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class CloudFrontLogsBucketLoggingConfiguration:
    resource: s3.bucket.LoggingConfiguration
    destination_bucket_name = ref(CloudFrontLogsLogBucket)


@cloudformation_dataclass
class CloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    bucket = get_att(CloudFrontLogsReplicaBucket, "Arn")


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationRule:
    resource: s3.bucket.ReplicationRule
    destination = CloudFrontLogsBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(CloudFrontLogsReplicationRole, "Arn")
    rules = [CloudFrontLogsBucketReplicationRule]


@cloudformation_dataclass
class CloudFrontLogsBucketDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Enabled'


@cloudformation_dataclass
class CloudFrontLogsBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_encryption = CloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = CloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = CloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = CloudFrontLogsBucketDeleteMarkerReplication
