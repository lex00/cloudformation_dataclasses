"""Storage resources: S3BucketSource."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.s3 import BucketVersioningStatus


@cloudformation_dataclass
class S3BucketSourceServerSideEncryptionByDefault:
    resource: s3.bucket.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AWS_KMS
    kms_master_key_id = ref(KmsKey)


@cloudformation_dataclass
class S3BucketSourceServerSideEncryptionRule:
    resource: s3.bucket.ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketSourceServerSideEncryptionByDefault
    bucket_key_enabled = True


@cloudformation_dataclass
class S3BucketSourceBucketEncryption:
    resource: s3.bucket.BucketEncryption
    server_side_encryption_configuration = [S3BucketSourceServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketSourcePublicAccessBlockConfiguration:
    resource: s3.multi_region_access_point.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3BucketSourceDeleteMarkerReplication:
    resource: s3.bucket.DeleteMarkerReplication
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class S3BucketSourceEncryptionConfiguration:
    resource: s3.bucket.EncryptionConfiguration
    replica_kms_key_id = Sub('arn:${AWS::Partition}:kms:${AWS::Region}:${AccountIdDestination}:alias/${AWS::StackName}-${AccountIdDestination}-kms-key')


@cloudformation_dataclass
class S3BucketSourceAccessControlTranslation:
    resource: s3.bucket.AccessControlTranslation
    owner = 'Destination'


@cloudformation_dataclass
class S3BucketSourceReplicationDestination:
    resource: s3.bucket.ReplicationDestination
    account = ref(AccountIdDestination)
    bucket = Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AccountIdDestination}-bucket')
    encryption_configuration = S3BucketSourceEncryptionConfiguration
    access_control_translation = S3BucketSourceAccessControlTranslation


@cloudformation_dataclass
class S3BucketSourceReplicationRuleFilter:
    resource: s3.bucket.ReplicationRuleFilter
    prefix = ''


@cloudformation_dataclass
class S3BucketSourceDeleteMarkerReplication1:
    resource: s3.bucket.DeleteMarkerReplication
    status = 'Disabled'


@cloudformation_dataclass
class S3BucketSourceSseKmsEncryptedObjects:
    resource: s3.bucket.SseKmsEncryptedObjects
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class S3BucketSourceSourceSelectionCriteria:
    resource: s3.bucket.SourceSelectionCriteria
    sse_kms_encrypted_objects = S3BucketSourceSseKmsEncryptedObjects


@cloudformation_dataclass
class S3BucketSourceReplicationRule:
    resource: s3.bucket.ReplicationRule
    id = 'Rule1'
    priority = 0
    status = ReplicationRuleStatus.ENABLED
    destination = S3BucketSourceReplicationDestination
    filter = S3BucketSourceReplicationRuleFilter
    delete_marker_replication = S3BucketSourceDeleteMarkerReplication1
    source_selection_criteria = S3BucketSourceSourceSelectionCriteria


@cloudformation_dataclass
class S3BucketSourceReplicationConfiguration:
    resource: s3.bucket.ReplicationConfiguration
    role = get_att(ReplicationRole, "Arn")
    rules = [S3BucketSourceReplicationRule]


@cloudformation_dataclass
class S3BucketSource:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('${AWS::StackName}-${AWS::AccountId}-bucket')
    bucket_encryption = S3BucketSourceBucketEncryption
    public_access_block_configuration = S3BucketSourcePublicAccessBlockConfiguration
    versioning_configuration = S3BucketSourceDeleteMarkerReplication
    replication_configuration = S3BucketSourceReplicationConfiguration
    deletion_policy = 'Delete'
