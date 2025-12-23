"""JwtResourceHandlerRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class JwtResourceHandlerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class JwtResourceHandlerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [JwtResourceHandlerRoleAllowStatement0]


@cloudformation_dataclass
class JwtResourceHandlerRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = JwtResourceHandlerRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']
