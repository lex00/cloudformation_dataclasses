"""Stack resources."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


@cloudformation_dataclass
class TransformFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = Runtime.PYTHON3_11
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
