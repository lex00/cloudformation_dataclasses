"""ReplicationRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


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
