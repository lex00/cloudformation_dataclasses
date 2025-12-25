"""Security resources: ECSRole, ECSTaskExecutionRole."""

from . import *  # noqa: F403


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
    resource: iam.user.Policy
    policy_name = 'AmazonECSTaskExecutionRolePolicy'
    policy_document = ECSTaskExecutionRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSTaskExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ECSTaskExecutionRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSTaskExecutionRolePolicy]
