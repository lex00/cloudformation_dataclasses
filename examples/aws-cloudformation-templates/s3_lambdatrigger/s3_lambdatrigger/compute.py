"""Compute resources: S3TriggerLambdaFunction, LambdaInvokePermission."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


@cloudformation_dataclass
class S3TriggerLambdaFunctionCode:
    resource: lambda_.function.Code
    zip_file = """import json
def lambda_handler(event,context):
    print(event)
    return "Hello... This is a test S3 trigger Lambda Function"
"""


@cloudformation_dataclass
class S3TriggerLambdaFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    code = S3TriggerLambdaFunctionCode
    handler = 'index.lambda_handler'
    role = get_att(LambdaIAMRole, "Arn")
    runtime = Runtime.PYTHON3_9
    timeout = 30


@cloudformation_dataclass
class LambdaInvokePermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    function_name = get_att(S3TriggerLambdaFunction, "Arn")
    action = 'lambda:InvokeFunction'
    principal = 's3.amazonaws.com'
    source_account = AWS_ACCOUNT_ID
    source_arn = Sub('arn:${AWS::Partition}:s3:::${NotificationBucket}')
