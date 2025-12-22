"""ECSEventRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSEventRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['events.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ECSEventRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSEventRoleAllowStatement0]


@cloudformation_dataclass
class ECSEventRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['ecs:RunTask']
    resource_arn = '*'


@cloudformation_dataclass
class ECSEventRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSEventRoleAllowStatement0_1]


@cloudformation_dataclass
class ECSEventRolePolicy:
    resource: Policy
    policy_name = 'ecs-service'
    policy_document = ECSEventRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSEventRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = ECSEventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSEventRolePolicy]
