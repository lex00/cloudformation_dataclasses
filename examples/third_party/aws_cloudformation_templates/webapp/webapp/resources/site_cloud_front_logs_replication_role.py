"""SiteCloudFrontLogsReplicationRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicationRoleAllowStatement0]


@cloudformation_dataclass
class SiteCloudFrontLogsReplicationRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument
    path = '/'
