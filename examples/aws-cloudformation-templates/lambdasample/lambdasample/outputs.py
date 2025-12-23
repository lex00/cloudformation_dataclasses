"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class LambdaRoleARNOutput:
    """Role for Lambda execution."""

    resource: Output
    value = get_att(LambdaRole, "Arn")
    description = 'Role for Lambda execution.'
    export_name = 'LambdaRole'


@cloudformation_dataclass
class LambdaFunctionNameOutput:
    resource: Output
    value = ref(LambdaFunction)


@cloudformation_dataclass
class LambdaFunctionARNOutput:
    """Lambda function ARN."""

    resource: Output
    value = get_att(LambdaFunction, "Arn")
    description = 'Lambda function ARN.'
    export_name = Sub('LambdaARN-${EnvName}')
