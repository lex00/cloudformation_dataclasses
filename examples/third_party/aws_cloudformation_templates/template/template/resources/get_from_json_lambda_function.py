from __future__ import annotations

"""GetFromJsonLambdaFunction - AWS::Serverless::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GetFromJsonLambdaFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    code_uri = '.'
    handler = 'getfromjson.lambda_handler'
    runtime = 'python3.12'
