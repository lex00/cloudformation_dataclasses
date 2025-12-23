"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TransformFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.11'
    handler = 'index.handler'
    memory_size = 128
    timeout = 3
    inline_code = """import datetime
def handler(event, context):
    response = {
        'requestId': event['requestId'],
        'status': 'success'
    }
    try:
        format = event['params']['format']
        response['fragment'] = datetime.datetime.now().strftime(format)
    except Exception as e:
        response['status'] = 'failure'
        response['errorMessage'] = str(e)
    return response
"""


@cloudformation_dataclass
class Transform:
    """AWS::CloudFormation::Macro resource."""

    # Unknown resource type: AWS::CloudFormation::Macro
    resource: CloudFormationResource
    name = 'DatetimeNow'
    description = 'Provides the current datetime as string in the format requested.'
    function_name = get_att(TransformFunction, "Arn")
