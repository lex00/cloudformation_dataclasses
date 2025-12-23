"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KmsKeyAllowStatement0:
    resource: PolicyStatement
    sid = 'Allow source account access to KMS key in source account'
    principal = {
        'AWS': Sub('arn:${AWS::Partition}:iam::${AWS::AccountId}:root'),
    }
    action = 'kms:*'
    resource_arn = '*'


@cloudformation_dataclass
class KmsKeyKeyPolicy:
    resource: PolicyDocument
    statement = [KmsKeyAllowStatement0]


@cloudformation_dataclass
class KmsKey:
    """AWS::KMS::Key resource."""

    resource: kms.Key
    enable_key_rotation = True
    key_policy = KmsKeyKeyPolicy


@cloudformation_dataclass
class KmsKeyAlias:
    """AWS::KMS::Alias resource."""

    resource: kms.Alias
    alias_name = Sub('alias/${AWS::StackName}-${AWS::AccountId}-kms-key')
    target_key_id = ref(KmsKey)


@cloudformation_dataclass
class ReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 's3.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class ReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ReplicationRoleAllowStatement0]


@cloudformation_dataclass
class ReplicationRoleAllowStatement0_1:
    resource: PolicyStatement
    sid = 'AllowActionsOnSourceBucket'
    action = [
        's3:ListBucket',
        's3:GetReplicationConfiguration',
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
    ]
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AWS::AccountId}-bucket/*'),
        Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AWS::AccountId}-bucket'),
    ]


@cloudformation_dataclass
class ReplicationRoleAllowStatement1:
    resource: PolicyStatement
    sid = 'AllowActionsOnDestinationBucket'
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicateTags',
        's3:GetObjectVersionTagging',
        's3:ObjectOwnerOverrideToBucketOwner',
    ]
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AccountIdDestination}-bucket/*'),
        Sub('arn:${AWS::Partition}:s3:::${AWS::StackName}-${AccountIdDestination}-bucket'),
    ]


@cloudformation_dataclass
class ReplicationRoleAllowStatement2:
    resource: PolicyStatement
    sid = 'AllowKmsDecryptOnSourceKey'
    action = 'kms:Decrypt'
    resource_arn = get_att(KmsKey, "Arn")


@cloudformation_dataclass
class ReplicationRoleAllowStatement3:
    resource: PolicyStatement
    sid = 'AllowKmsEncryptOnDestinationKey'
    action = 'kms:Encrypt'
    resource_arn = '*'
    condition = {
        STRING_EQUALS: {
            'kms:RequestAlias': Sub('alias/${AWS::StackName}-${AccountIdDestination}-kms-key'),
        },
    }


@cloudformation_dataclass
class ReplicationRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ReplicationRoleAllowStatement0_1, ReplicationRoleAllowStatement1, ReplicationRoleAllowStatement2, ReplicationRoleAllowStatement3]


@cloudformation_dataclass
class ReplicationRolePolicy:
    resource: iam.user.Policy
    policy_name = Sub('${AWS::StackName}-${AccountIdDestination}-role-policy')
    policy_document = ReplicationRolePolicies0PolicyDocument


@cloudformation_dataclass
class ReplicationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = Sub('${AWS::StackName}-${AccountIdDestination}-role')
    description = 'IAM Role used by S3 bucket replication'
    assume_role_policy_document = ReplicationRoleAssumeRolePolicyDocument
    policies = [ReplicationRolePolicy]


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
    status = 'Enabled'


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
    status = 'Enabled'


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
