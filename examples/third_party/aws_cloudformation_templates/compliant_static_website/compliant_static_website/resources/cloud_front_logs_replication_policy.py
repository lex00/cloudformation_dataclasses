from __future__ import annotations

"""CloudFrontLogsReplicationPolicy - AWS::IAM::RolePolicy resource."""

from .. import *  # noqa: F403


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

    resource: RolePolicy
    policy_document = CloudFrontLogsReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(CloudFrontLogsReplicationRole)
