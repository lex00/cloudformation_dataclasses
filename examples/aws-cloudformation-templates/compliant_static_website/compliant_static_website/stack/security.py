"""Security resources: CloudFrontLogsReplicationRole, CloudFrontLogsReplicationPolicy, ContentReplicationRole, ContentReplicationPolicy."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFrontLogsReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class CloudFrontLogsReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsReplicationRoleAllowStatement0]


@cloudformation_dataclass
class CloudFrontLogsReplicationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = CloudFrontLogsReplicationRoleAssumeRolePolicyDocument
    path = '/'


@cloudformation_dataclass
class CloudFrontLogsReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')


@cloudformation_dataclass
class CloudFrontLogsReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class CloudFrontLogsReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class CloudFrontLogsReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [CloudFrontLogsReplicationPolicyAllowStatement0, CloudFrontLogsReplicationPolicyAllowStatement1, CloudFrontLogsReplicationPolicyAllowStatement2]


@cloudformation_dataclass
class CloudFrontLogsReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_document = CloudFrontLogsReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(CloudFrontLogsReplicationRole)


@cloudformation_dataclass
class ContentReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ContentReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ContentReplicationRoleAllowStatement0]


@cloudformation_dataclass
class ContentReplicationRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ContentReplicationRoleAssumeRolePolicyDocument
    path = '/'


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

    resource: iam.RolePolicy
    policy_document = ContentReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(ContentReplicationRole)
