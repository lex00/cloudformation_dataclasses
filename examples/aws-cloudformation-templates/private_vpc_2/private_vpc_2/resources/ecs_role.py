"""ECSRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ecs.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class ECSRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ECSRoleAllowStatement0]


@cloudformation_dataclass
class ECSRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ec2:AttachNetworkInterface',
        'ec2:CreateNetworkInterface',
        'ec2:CreateNetworkInterfacePermission',
        'ec2:DeleteNetworkInterface',
        'ec2:DeleteNetworkInterfacePermission',
        'ec2:Describe*',
        'ec2:DetachNetworkInterface',
        'elasticloadbalancing:DeregisterInstancesFromLoadBalancer',
        'elasticloadbalancing:DeregisterTargets',
        'elasticloadbalancing:Describe*',
        'elasticloadbalancing:RegisterInstancesWithLoadBalancer',
        'elasticloadbalancing:RegisterTargets',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class ECSRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ECSRoleAllowStatement0_1]


@cloudformation_dataclass
class ECSRolePolicy:
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = ECSRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ECSRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSRolePolicy]
