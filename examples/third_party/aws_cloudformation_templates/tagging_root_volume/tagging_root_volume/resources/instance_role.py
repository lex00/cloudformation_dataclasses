from __future__ import annotations

"""InstanceRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class InstanceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [InstanceRoleAllowStatement0]


@cloudformation_dataclass
class InstanceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ec2:Describe*',
        'ec2:CreateTags',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class InstanceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [InstanceRoleAllowStatement0_1]


@cloudformation_dataclass
class InstanceRolePolicy:
    resource: Policy
    policy_name = 'taginstancepolicy'
    policy_document = InstanceRolePolicies0PolicyDocument


@cloudformation_dataclass
class InstanceRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = InstanceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [InstanceRolePolicy]
