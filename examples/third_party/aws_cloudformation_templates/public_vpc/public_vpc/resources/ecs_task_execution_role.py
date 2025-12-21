from __future__ import annotations

"""ECSTaskExecutionRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSTaskExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs-tasks.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ECSTaskExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSTaskExecutionRoleAllowStatement0]


@cloudformation_dataclass
class ECSTaskExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ecr:GetAuthorizationToken',
        'ecr:BatchCheckLayerAvailability',
        'ecr:GetDownloadUrlForLayer',
        'ecr:BatchGetImage',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ECSTaskExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSTaskExecutionRoleAllowStatement0_1]


@cloudformation_dataclass
class ECSTaskExecutionRolePolicy:
    resource: Policy
    policy_name = 'AmazonECSTaskExecutionRolePolicy'
    policy_document = ECSTaskExecutionRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSTaskExecutionRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = ECSTaskExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSTaskExecutionRolePolicy]
