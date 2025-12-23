"""ECSServiceRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSServiceRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ECSServiceRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSServiceRoleAllowStatement0]


@cloudformation_dataclass
class ECSServiceRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'elasticloadbalancing:DeregisterInstancesFromLoadBalancer',
        'elasticloadbalancing:DeregisterTargets',
        'elasticloadbalancing:Describe*',
        'elasticloadbalancing:RegisterInstancesWithLoadBalancer',
        'elasticloadbalancing:RegisterTargets',
        'ec2:Describe*',
        'ec2:AuthorizeSecurityGroupIngress',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ECSServiceRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSServiceRoleAllowStatement0_1]


@cloudformation_dataclass
class ECSServiceRolePolicy:
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = ECSServiceRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSServiceRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ECSServiceRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSServiceRolePolicy]
