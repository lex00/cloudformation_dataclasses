from __future__ import annotations

"""SiteCloudFrontLogsReplicationPolicy - AWS::IAM::RolePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicationPolicyAllowStatement0, SiteCloudFrontLogsReplicationPolicyAllowStatement1, SiteCloudFrontLogsReplicationPolicyAllowStatement2]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationPolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: RolePolicy
    policy_document = SiteCloudFrontLogsReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = ref(SiteCloudFrontLogsReplicationRole)
