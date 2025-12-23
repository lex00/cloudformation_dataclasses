"""Stack resources."""

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


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    # Unknown resource type: AWS::CloudFormation::Macro
    resource: CloudFormationResource
    name = 'Count'
    function_name = get_att(CountMacroFunction, "Arn")
