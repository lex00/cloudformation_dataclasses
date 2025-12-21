from __future__ import annotations

"""RootRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RootRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class RootRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [RootRoleAllowStatement0]


@cloudformation_dataclass
class RootRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 'cloudformation:*'
    resource_arn = '*'


@cloudformation_dataclass
class RootRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [RootRoleAllowStatement0_1]


@cloudformation_dataclass
class RootRolePolicy:
    resource: Policy
    policy_name = 'root'
    policy_document = RootRolePolicies0PolicyDocument


@cloudformation_dataclass
class RootRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = RootRoleAssumeRolePolicyDocument
    path = '/'
    policies = [RootRolePolicy]
