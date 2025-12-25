"""Stack resources."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


@cloudformation_dataclass
class CountMacroFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    code_uri = 'src'
    handler = 'index.handler'
    runtime = Runtime.PYTHON3_11
    timeout = 5
