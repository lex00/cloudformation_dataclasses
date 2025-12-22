"""CloudFrontLogsReplicationRole - AWS::IAM::Role resource."""

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

    resource: Role
    assume_role_policy_document = CloudFrontLogsReplicationRoleAssumeRolePolicyDocument
    path = '/'
