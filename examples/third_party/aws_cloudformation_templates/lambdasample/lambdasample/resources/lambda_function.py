from __future__ import annotations

"""LambdaFunction - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaFunctionCode:
    resource: Code
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
    resource: Environment
    variables = {
        'ENV': ref(EnvName),
        'TZ': 'UTC',
    }


@cloudformation_dataclass
class LambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: Function
    function_name = Sub('lambda-function-${EnvName}')
    description = 'LambdaFunction using python3.12.'
    runtime = 'python3.12'
    code = LambdaFunctionCode
    handler = Sub('${LambdaHandlerPath}')
    memory_size = 128
    timeout = 10
    role = get_att(LambdaRole, "Arn")
    environment = LambdaFunctionEnvironment
