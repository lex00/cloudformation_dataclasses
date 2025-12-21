from __future__ import annotations

"""EMRClusterinstanceProfileRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EMRClusterinstanceProfileRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class EMRClusterinstanceProfileRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EMRClusterinstanceProfileRoleAllowStatement0]


@cloudformation_dataclass
class EMRClusterinstanceProfileRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = EMRClusterinstanceProfileRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role']
    path = '/'
