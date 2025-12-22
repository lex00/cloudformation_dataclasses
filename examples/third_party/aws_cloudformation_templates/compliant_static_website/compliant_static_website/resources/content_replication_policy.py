"""ContentReplicationPolicy - AWS::IAM::RolePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ContentReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}')


@cloudformation_dataclass
class ContentReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class ContentReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-replicas-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class ContentReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [ContentReplicationPolicyAllowStatement0, ContentReplicationPolicyAllowStatement1, ContentReplicationPolicyAllowStatement2]


@cloudformation_dataclass
class ContentReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: RolePolicy
    policy_document = ContentReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(ContentReplicationRole)
