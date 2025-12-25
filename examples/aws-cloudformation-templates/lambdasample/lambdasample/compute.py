"""Compute resources: LambdaFunction."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


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
    runtime = Runtime.PYTHON3_12
    code = LambdaFunctionCode
    handler = Sub('${LambdaHandlerPath}')
    memory_size = 128
    timeout = 10
    role = get_att(LambdaRole, "Arn")
    environment = LambdaFunctionEnvironment
