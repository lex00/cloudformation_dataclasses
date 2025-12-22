"""MyLambdaRole - AWS::IAM::Role resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class MyLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [MyLambdaRoleAllowStatement0]


@cloudformation_dataclass
class MyLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    action = ['logs:CreateLogGroup']
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:*')


@cloudformation_dataclass
class MyLambdaRoleAllowStatement1:
    resource: PolicyStatement
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/lambda/${AWS::StackName}:*')


@cloudformation_dataclass
class MyLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [MyLambdaRoleAllowStatement0_1, MyLambdaRoleAllowStatement1]


@cloudformation_dataclass
class MyLambdaRolePolicy:
    resource: Policy
    policy_name = ref(MyLambda)
    policy_document = MyLambdaRolePolicies0PolicyDocument


@cloudformation_dataclass
class MyLambdaRole:
    """AWS::IAM::Role resource."""

    resource: Role
    assume_role_policy_document = MyLambdaRoleAssumeRolePolicyDocument
    path = '/'
    policies = [MyLambdaRolePolicy]
