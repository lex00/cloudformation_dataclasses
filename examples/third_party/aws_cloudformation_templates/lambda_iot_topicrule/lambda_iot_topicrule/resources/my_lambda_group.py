"""Grouped resources: MyLambda, MyLambdaRole."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyLambdaCode:
    resource: lambda_.Code
    zip_file = """exports.handler = async (event) => { console.log(event); return {'statusCode': 200, 'body': "OK"}; }
"""


@cloudformation_dataclass
class MyLambda:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    runtime = 'nodejs20.x'
    handler = 'index.handler'
    code = MyLambdaCode
    function_name = Sub('${AWS::StackName}')
    role = get_att("MyLambdaRole", "Arn")


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
    resource: iam.Policy
    policy_name = ref(MyLambda)
    policy_document = MyLambdaRolePolicies0PolicyDocument


@cloudformation_dataclass
class MyLambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = MyLambdaRoleAssumeRolePolicyDocument
    path = '/'
    policies = [MyLambdaRolePolicy]
