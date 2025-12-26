"""Security resources: ObjectStorageReplicationRole, ObjectStorageReplicationPolicy."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ObjectStorageReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ObjectStorageReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageReplicationRoleAllowStatement0]


@cloudformation_dataclass
class ObjectStorageReplicationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ObjectStorageReplicationRoleAssumeRolePolicyDocument
    path = '/'


@cloudformation_dataclass
class ObjectStorageReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}')


@cloudformation_dataclass
class ObjectStorageReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class ObjectStorageReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class ObjectStorageReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ObjectStorageReplicationPolicyAllowStatement0, ObjectStorageReplicationPolicyAllowStatement1, ObjectStorageReplicationPolicyAllowStatement2]


@cloudformation_dataclass
class ObjectStorageReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = ObjectStorageReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(ObjectStorageReplicationRole)
