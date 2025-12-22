"""LambdaExecutionRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaExecutionRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0]


@cloudformation_dataclass
class LambdaExecutionRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:*',
        'config:PutEvaluations',
        'ec2:DescribeVolumeAttribute',
    ]
    resource_arn = '*'


@cloudformation_dataclass
class LambdaExecutionRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaExecutionRoleAllowStatement0_1]


@cloudformation_dataclass
class LambdaExecutionRolePolicy:
    resource: iam.user.Policy
    policy_name = 'root'
    policy_document = LambdaExecutionRolePolicies0PolicyDocument


@cloudformation_dataclass
class LambdaExecutionRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = LambdaExecutionRoleAssumeRolePolicyDocument
    policies = [LambdaExecutionRolePolicy]
