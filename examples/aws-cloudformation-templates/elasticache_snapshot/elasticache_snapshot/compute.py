"""Compute resources: EnableShapshot, LambdaExecutePermission."""

from . import *  # noqa: F403

from cloudformation_dataclasses.aws.lambda_ import Runtime


@cloudformation_dataclass
class EnableShapshotCode:
    resource: lambda_.function.Code
    zip_file = {
        'Rain::Embed': 'elastic-code.js',
    }


@cloudformation_dataclass
class EnableShapshot:
    """AWS::Lambda::Function resource."""

    resource: lambda_.Function
    code = EnableShapshotCode
    handler = 'index.handler'
    memory_size = 128
    role = get_att(IamRoleLambda, "Arn")
    runtime = Runtime.NODEJS20_X
    timeout = 30
    depends_on = ["IamRoleLambda"]
    condition = 'EnableBackups'
    deletion_policy = 'Delete'


@cloudformation_dataclass
class LambdaExecutePermission:
    """AWS::Lambda::Permission resource."""

    resource: lambda_.Permission
    action = 'lambda:InvokeFunction'
    function_name = get_att(EnableShapshot, "Arn")
    principal = 'elasticache.amazonaws.com'
    source_account = Sub('${AWS::AccountId}')
    condition = 'EnableBackups'
