"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Function:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.11'
    code_uri = 'lambda'
    handler = 'index.handler'


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = 'ExecutionRoleBuilder'
    function_name = get_att(Function, "Arn")
