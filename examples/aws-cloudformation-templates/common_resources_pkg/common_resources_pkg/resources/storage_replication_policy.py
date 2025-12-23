"""StorageReplicationPolicy - AWS::IAM::RolePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class StorageReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}')


@cloudformation_dataclass
class StorageReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class StorageReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class StorageReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [StorageReplicationPolicyAllowStatement0, StorageReplicationPolicyAllowStatement1, StorageReplicationPolicyAllowStatement2]


@cloudformation_dataclass
class StorageReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = StorageReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(StorageReplicationRole)
