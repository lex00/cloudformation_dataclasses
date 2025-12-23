"""Compute resources: TransformFunction, TransformFunctionPermissions."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TransformFunctionCode:
    resource: lambda_.function.Code
    zip_file = {
        'Rain::Embed': 'handler.py',
    }


@cloudformation_dataclass
class TransformFunction:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    code = TransformFunctionCode
    handler = 'index.handler'
    runtime = 'python3.12'
    role = get_att(TransformExecutionRole, "Arn")


@cloudformation_dataclass
class TransformFunctionPermissions:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(TransformFunction, "Arn")
    principal = 'cloudformation.amazonaws.com'
