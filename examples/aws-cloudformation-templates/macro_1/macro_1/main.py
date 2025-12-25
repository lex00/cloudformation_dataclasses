"""Stack resources."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


@cloudformation_dataclass
class ResourceFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'PowerUserAccess'


@cloudformation_dataclass
class MacroFunctionEnvironment:
    resource: lambda_.function.Environment
    variables = {
        'LAMBDA_ARN': get_att(ResourceFunction, "Arn"),
    }


@cloudformation_dataclass
class MacroFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = Runtime.PYTHON3_11
    code_uri = 'lambda'
    handler = 'macro.handler'
    environment = MacroFunctionEnvironment
