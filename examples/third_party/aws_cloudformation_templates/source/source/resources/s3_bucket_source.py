"""S3BucketSource - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketSourceServerSideEncryptionByDefault:
    resource: s3.ServerSideEncryptionByDefault
    sse_algorithm = ServerSideEncryption.AWS_KMS
    kms_master_key_id = ref(KmsKey)


@cloudformation_dataclass
class S3BucketSourceServerSideEncryptionRule:
    resource: s3.ServerSideEncryptionRule
    server_side_encryption_by_default = S3BucketSourceServerSideEncryptionByDefault
    bucket_key_enabled = True


@cloudformation_dataclass
class S3BucketSourceBucketEncryption:
    resource: s3.BucketEncryption
    server_side_encryption_configuration = [S3BucketSourceServerSideEncryptionRule]


@cloudformation_dataclass
class S3BucketSourcePublicAccessBlockConfiguration:
    resource: s3.PublicAccessBlockConfiguration
    block_public_acls = True
    block_public_policy = True
    ignore_public_acls = True
    restrict_public_buckets = True


@cloudformation_dataclass
class S3BucketSourceVersioningConfiguration:
    resource: s3.VersioningConfiguration
    status = BucketVersioningStatus.ENABLED


@cloudformation_dataclass
class S3BucketSourceEncryptionConfiguration:
    resource: s3.EncryptionConfiguration
    replica_kms_key_id = Sub('arn:${AWS::Partition}:kms:${AWS::Region}:${AccountIdDestination}:alias/${AWS::StackName}-${AccountIdDestination}-kms-key')


@cloudformation_dataclass
class S3BucketSourceAccessControlTranslation:
    resource: AccessControlTranslation
    owner = 'Destination'


@cloudformation_dataclass
class S3BucketSourceReplicationDestination:
    resource: s3.ReplicationDestination
    account = ref(AccountIdDestination)
    bucket = Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AccountIdDestination}-bucket')
    encryption_configuration = S3BucketSourceEncryptionConfiguration
    access_control_translation = S3BucketSourceAccessControlTranslation


@cloudformation_dataclass
class S3BucketSourceReplicationRuleFilter:
    resource: ReplicationRuleFilter
    prefix = ''


@cloudformation_dataclass
class S3BucketSourceDeleteMarkerReplication:
    resource: DeleteMarkerReplication
    status = 'Disabled'


@cloudformation_dataclass
class S3BucketSourceSseKmsEncryptedObjects:
    resource: SseKmsEncryptedObjects
    status = 'Enabled'


@cloudformation_dataclass
class S3BucketSourceSourceSelectionCriteria:
    resource: SourceSelectionCriteria
    sse_kms_encrypted_objects = S3BucketSourceSseKmsEncryptedObjects


@cloudformation_dataclass
class S3BucketSourceReplicationRule:
    resource: s3.ReplicationRule
    id = 'Rule1'
    priority = 0
    status = ReplicationRuleStatus.ENABLED
    destination = S3BucketSourceReplicationDestination
    filter = S3BucketSourceReplicationRuleFilter
    delete_marker_replication = S3BucketSourceDeleteMarkerReplication
    source_selection_criteria = S3BucketSourceSourceSelectionCriteria


@cloudformation_dataclass
class S3BucketSourceReplicationConfiguration:
    resource: s3.ReplicationConfiguration
    role = get_att(ReplicationRole, "Arn")
    rules = [S3BucketSourceReplicationRule]


@cloudformation_dataclass
class S3BucketSource:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    bucket_name = Sub('${AWS::StackName}-${AWS::AccountId}-bucket')
    bucket_encryption = S3BucketSourceBucketEncryption
    public_access_block_configuration = S3BucketSourcePublicAccessBlockConfiguration
    versioning_configuration = S3BucketSourceVersioningConfiguration
    replication_configuration = S3BucketSourceReplicationConfiguration
    deletion_policy = 'Delete'
