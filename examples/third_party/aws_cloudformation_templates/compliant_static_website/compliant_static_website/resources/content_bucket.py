from __future__ import annotations

"""ContentBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ContentBucketServerSideEncryptionByDefault:
    resource: ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AES256


@cloudformation_dataclass
class ContentBucketServerSideEncryptionRule:
    resource: ServerSideEncryptionRule
    server_side_encryption_by_default = ContentBucketServerSideEncryptionByDefault


@cloudformation_dataclass
class ContentBucketBucketEncryption:
    resource: BucketEncryption
    server_side_encryption_configuration = [ContentBucketServerSideEncryptionRule]


@cloudformation_dataclass
class ContentBucketLoggingConfiguration:
    resource: LoggingConfiguration
    destination_bucket_name = ref(ContentLogBucket)


@cloudformation_dataclass
class ContentBucketPublicAccessBlockConfiguration:
    resource: PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class ContentBucketReplicationDestination:
    resource: ReplicationDestination
    bucket = get_att(ContentReplicaBucket, "Arn")


@cloudformation_dataclass
class ContentBucketReplicationRule:
    resource: ReplicationRule
    destination = ContentBucketReplicationDestination
    status = ReplicationRuleStatus.ENABLED


@cloudformation_dataclass
class ContentBucketReplicationConfiguration:
    resource: ReplicationConfiguration
    role = get_att(ContentReplicationRole, "Arn")
    rules = [ContentBucketReplicationRule]


@cloudformation_dataclass
class ContentBucketVersioningConfiguration:
    resource: VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class ContentBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    bucket_encryption = ContentBucketBucketEncryption
    bucket_name = Sub('${AppName}-${AWS::Region}-${AWS::AccountId}')
    logging_configuration = ContentBucketLoggingConfiguration
    object_lock_enabled = False
    public_access_block_configuration = ContentBucketPublicAccessBlockConfiguration
    replication_configuration = ContentBucketReplicationConfiguration
    versioning_configuration = ContentBucketVersioningConfiguration
