from __future__ import annotations

"""CloudFrontLogsBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontLogsBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class CloudFrontLogsBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = CloudFrontLogsBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class CloudFrontLogsBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [CloudFrontLogsBucketServerSideEncryptionRule]


@cloudformation_dataclass
class CloudFrontLogsBucketLoggingConfiguration:
    resource: LoggingConfiguration
    destination_bucket_name: Ref[CloudFrontLogsLogBucket] = ref()


@cloudformation_dataclass
class CloudFrontLogsBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationDestination:
    resource: ReplicationDestination
    bucket: GetAtt[CloudFrontLogsReplicaBucket] = get_att("Arn")


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationRule:
    resource: ReplicationRule
    destination = CloudFrontLogsBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsBucketReplicationConfiguration:
    resource: ReplicationConfiguration
    role: GetAtt[CloudFrontLogsReplicationRole] = get_att("Arn")
    rules = [CloudFrontLogsBucketReplicationRule]


@cloudformation_dataclass
class CloudFrontLogsBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class CloudFrontLogsBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = CloudFrontLogsBucketBucketEncryption
    bucket_name = Sub('${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = CloudFrontLogsBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = CloudFrontLogsBucketPublicAccessBlockConfiguration
    replication_configuration = CloudFrontLogsBucketReplicationConfiguration
    versioning_configuration = CloudFrontLogsBucketVersioningConfiguration
