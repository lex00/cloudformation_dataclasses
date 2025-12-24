"""Security resources: LogsKmsKey, EC2Role, EC2InstanceProfile, ECSServiceRole, ECSEventRole, AutoscalingRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LogsKmsKey:
    """AWS::KMS::Key resource."""

    resource: kms.Key
    description = 'ECS Logs Encryption Key'
    enable_key_rotation = True


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
    resource: iam.user.Policy
    policy_name = 'ecs-service'
    policy_document = ECSEventRolePolicies0PolicyDocument


@cloudformation_dataclass
class ECSEventRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = ECSEventRoleAssumeRolePolicyDocument
    path = '/'
    policies = [ECSEventRolePolicy]


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
