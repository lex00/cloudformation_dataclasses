from __future__ import annotations

"""S3TriggerLambdaFunction - AWS::Lambda::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3TriggerLambdaFunctionCode:
    resource: Code
    zip_file = """import json
def lambda_handler(event,context):
    print(event)
    return "Hello... This is a test S3 trigger Lambda Function"
"""


@cloudformation_dataclass
class S3TriggerLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: Function
    code = S3TriggerLambdaFunctionCode
    handler = 'index.lambda_handler'
    role = get_att(LambdaIAMRole, "Arn")
    runtime = 'python3.9'
    timeout = 30
