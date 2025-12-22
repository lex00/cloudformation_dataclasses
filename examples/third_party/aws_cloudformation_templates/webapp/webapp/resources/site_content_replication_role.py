"""SiteContentReplicationRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SiteContentReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class SiteContentReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentReplicationRoleAllowStatement0]


@cloudformation_dataclass
class SiteContentReplicationRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = SiteContentReplicationRoleAssumeRolePolicyDocument
    path = '/'
