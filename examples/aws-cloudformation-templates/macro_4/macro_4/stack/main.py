"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ResourceFunction:
    """AWS::Serverless::Function resource."""

    # Unknown resource type: AWS::Serverless::Function
    resource: CloudFormationResource
    runtime = 'python3.11'
    code_uri = 'lambda'
    handler = 'resource.handler'
    policies = 'AmazonS3FullAccess'


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
    runtime = 'python3.11'
    code_uri = 'lambda'
    handler = 'macro.handler'
    policies = 'AmazonS3FullAccess'
    environment = MacroFunctionEnvironment


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = 'S3Objects'
    function_name = get_att(MacroFunction, "Arn")
