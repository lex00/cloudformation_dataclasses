from __future__ import annotations

"""AutoscalingRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AutoscalingRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['application-autoscaling.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class AutoscalingRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AutoscalingRoleAllowStatement0]


@cloudformation_dataclass
class AutoscalingRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'application-autoscaling:*',
        'cloudwatch:DescribeAlarms',
        'cloudwatch:PutMetricAlarm',
        'ecs:DescribeServices',
        'ecs:UpdateService',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class AutoscalingRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AutoscalingRoleAllowStatement0_1]


@cloudformation_dataclass
class AutoscalingRolePolicy:
    resource: Policy
    policy_name = 'service-autoscaling'
    policy_document = AutoscalingRolePolicies0PolicyDocument


@cloudformation_dataclass
class AutoscalingRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = AutoscalingRoleAssumeRolePolicyDocument
    path = '/'
    policies = [AutoscalingRolePolicy]
