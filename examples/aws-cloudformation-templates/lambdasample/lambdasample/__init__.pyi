"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iam, lambda_
from cloudformation_dataclasses.intrinsics import Sub
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import LambdaFunction as LambdaFunction
from .compute import LambdaFunctionCode as LambdaFunctionCode
from .compute import LambdaFunctionEnvironment as LambdaFunctionEnvironment
from .outputs import LambdaFunctionARNOutput as LambdaFunctionARNOutput
from .outputs import LambdaFunctionNameOutput as LambdaFunctionNameOutput
from .outputs import LambdaRoleARNOutput as LambdaRoleARNOutput
from .params import EnvName as EnvName
from .params import LambdaHandlerPath as LambdaHandlerPath
from .security import LambdaRole as LambdaRole
from .security import LambdaRoleAllowStatement0 as LambdaRoleAllowStatement0
from .security import LambdaRoleAssumeRolePolicyDocument as LambdaRoleAssumeRolePolicyDocument

__all__: list[str] = ['EnvName', 'LambdaFunction', 'LambdaFunctionARNOutput', 'LambdaFunctionCode', 'LambdaFunctionEnvironment', 'LambdaFunctionNameOutput', 'LambdaHandlerPath', 'LambdaRole', 'LambdaRoleARNOutput', 'LambdaRoleAllowStatement0', 'LambdaRoleAssumeRolePolicyDocument', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'STRING', 'Sub', 'Template', 'cloudformation_dataclass', 'get_att', 'iam', 'lambda_', 'ref', 'setup_resources']
