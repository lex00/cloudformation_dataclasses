"""ContentReplicationRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


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
