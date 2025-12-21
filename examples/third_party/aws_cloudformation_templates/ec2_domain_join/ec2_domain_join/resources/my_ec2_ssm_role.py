from __future__ import annotations

"""myEC2SSMRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class myEC2SSMRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class myEC2SSMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [myEC2SSMRoleAllowStatement0]


@cloudformation_dataclass
class myEC2SSMRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = myEC2SSMRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM']
    role_name = 'DemoEC2SSMRole'
