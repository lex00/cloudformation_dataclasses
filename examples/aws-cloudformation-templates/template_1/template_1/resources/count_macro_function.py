"""CountMacroFunction - AWS::Serverless::Function resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CountMacroFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    code_uri = 'src'
    handler = 'index.handler'
    runtime = 'python3.11'
    timeout = 5
