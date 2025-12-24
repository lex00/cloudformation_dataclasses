"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ResourceFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.12'
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'CloudWatchFullAccess'


@cloudformation_dataclass
class MacroFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.12'
    code_uri = 'lambda'
    handler = 'index.handler'
