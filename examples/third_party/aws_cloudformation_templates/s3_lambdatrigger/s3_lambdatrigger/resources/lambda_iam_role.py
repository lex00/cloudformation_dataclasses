"""LambdaIAMRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaIAMRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaIAMRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIAMRoleAllowStatement0]


@cloudformation_dataclass
class LambdaIAMRoleAllowStatement0_1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogGroup',
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = 'arn:aws:logs:*:*:*'


@cloudformation_dataclass
class LambdaIAMRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIAMRoleAllowStatement0_1]


@cloudformation_dataclass
class LambdaIAMRolePolicy:
    resource: iam.Policy
    policy_name = 'root'
    policy_document = LambdaIAMRolePolicies0PolicyDocument


@cloudformation_dataclass
class LambdaIAMRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = LambdaIAMRoleAssumeRolePolicyDocument
    path = '/'
    policies = [LambdaIAMRolePolicy]
