"""Security resources: LambdaIamRole."""

from . import *  # noqa: F403


@cloudformation_dataclass
class LambdaIamRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaIamRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIamRoleAllowStatement0]


@cloudformation_dataclass
class LambdaIamRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['logs:CreateLogGroup']
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:*')


@cloudformation_dataclass
class LambdaIamRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/${LambdaFunctionName}:*')


@cloudformation_dataclass
class LambdaIamRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [LambdaIamRoleAllowStatement0_1, LambdaIamRoleAllowStatement1]


@cloudformation_dataclass
class LambdaIamRolePolicy:
    resource: iam.user.Policy
    policy_name = 'LambdaApipolicy'
    policy_document = LambdaIamRolePolicies0PolicyDocument


@cloudformation_dataclass
class LambdaIamRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = LambdaIamRoleAssumeRolePolicyDocument
    role_name = 'LambdaRole'
    policies = [LambdaIamRolePolicy]
