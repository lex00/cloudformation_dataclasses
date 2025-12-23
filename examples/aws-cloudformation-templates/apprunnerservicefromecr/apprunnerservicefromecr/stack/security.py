"""Security resources: AppRunnerRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AppRunnerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['build.apprunner.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class AppRunnerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [AppRunnerRoleAllowStatement0]


@cloudformation_dataclass
class AppRunnerRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'ecr:GetDownloadUrlForLayer',
        'ecr:BatchGetImage',
        'ecr:DescribeImages',
        'ecr:GetAuthorizationToken',
        'ecr:BatchCheckLayerAvailability',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class AppRunnerRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [AppRunnerRoleAllowStatement0_1]


@cloudformation_dataclass
class AppRunnerRolePolicy:
    resource: iam.user.Policy
    policy_name = 'root'
    policy_document = AppRunnerRolePolicies0PolicyDocument


@cloudformation_dataclass
class AppRunnerRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = AppRunnerRoleAssumeRolePolicyDocument
    path = '/'
    policies = [AppRunnerRolePolicy]
