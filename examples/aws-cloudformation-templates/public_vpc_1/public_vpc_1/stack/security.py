"""Security resources: EC2Role, EC2InstanceProfile, AutoscalingRole, ECSRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2RoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class EC2RoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EC2RoleAllowStatement0]


@cloudformation_dataclass
class EC2RoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ecs:CreateCluster',
        'ecs:DeregisterContainerInstance',
        'ecs:DiscoverPollEndpoint',
        'ecs:Poll',
        'ecs:RegisterContainerInstance',
        'ecs:StartTelemetrySession',
        'ecs:Submit*',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
        'ecr:GetAuthorizationToken',
        'ecr:BatchGetImage',
        'ecr:GetDownloadUrlForLayer',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class EC2RolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [EC2RoleAllowStatement0_1]


@cloudformation_dataclass
class EC2RolePolicy:
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = EC2RolePolicies0PolicyDocument


@cloudformation_dataclass
class EC2Role:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EC2RoleAssumeRolePolicyDocument
    path = '/'
    policies = [EC2RolePolicy]


@cloudformation_dataclass
class EC2InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    path = '/'
    roles = [ref(EC2Role)]


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
    resource: iam.user.Policy
    policy_name = 'service-autoscaling'
    policy_document = AutoscalingRolePolicies0PolicyDocument


@cloudformation_dataclass
class AutoscalingRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = AutoscalingRoleAssumeRolePolicyDocument
    path = '/'
    policies = [AutoscalingRolePolicy]


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
