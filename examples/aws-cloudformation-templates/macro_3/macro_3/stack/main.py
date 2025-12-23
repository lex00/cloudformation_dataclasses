"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MacroFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.11'
    code_uri = 'lambda'
    handler = 'explode.handler'


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = 'Explode'
    function_name = get_att(MacroFunction, "Arn")
