"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


@cloudformation_dataclass
class LambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [LambdaRoleAllowStatement0]


@cloudformation_dataclass
class LambdaRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    role_name = 'lambda-role'
    assume_role_policy_document = LambdaRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/AWSLambdaExecute', 'arn:aws:iam::aws:policy/AmazonS3FullAccess', 'arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess', 'arn:aws:iam::aws:policy/AmazonKinesisFullAccess']
    path = '/'


@cloudformation_dataclass
class LambdaFunctionCode:
    resource: lambda_.function.Code
    zip_file = """import json

def lambda_handler(event, context):
    print(json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
"""


@cloudformation_dataclass
class LambdaFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'ENV': ref(EnvName),
        'TZ': 'UTC',
    }


@cloudformation_dataclass
class LambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    function_name = Sub('lambda-function-${EnvName}')
    description = 'LambdaFunction using python3.12.'
    runtime = 'python3.12'
    code = LambdaFunctionCode
    handler = Sub('${LambdaHandlerPath}')
    memory_size = 128
    timeout = 10
    role = get_att(LambdaRole, "Arn")
    environment = LambdaFunctionEnvironment
