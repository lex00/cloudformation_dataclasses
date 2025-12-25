"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Parameter,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation, iam, lambda_
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    Equals,
    If,
    Not,
    Sub,
)
from .params import *  # noqa: F403, F401

from .compute import TransformFunction as TransformFunction
from .compute import TransformFunctionCode as TransformFunctionCode
from .compute import TransformFunctionPermissions as TransformFunctionPermissions
from .infra import Transform as Transform
from .params import AdditionalExecutionPolicy as AdditionalExecutionPolicy
from .params import AdditionalPolicyProvidedCondition as AdditionalPolicyProvidedCondition
from .params import LambdaTimeout as LambdaTimeout
from .security import TransformExecutionRole as TransformExecutionRole
from .security import TransformExecutionRoleAllowStatement0 as TransformExecutionRoleAllowStatement0
from .security import TransformExecutionRoleAllowStatement0_1 as TransformExecutionRoleAllowStatement0_1
from .security import TransformExecutionRoleAssumeRolePolicyDocument as TransformExecutionRoleAssumeRolePolicyDocument
from .security import TransformExecutionRolePolicies0PolicyDocument as TransformExecutionRolePolicies0PolicyDocument
from .security import TransformExecutionRolePolicy as TransformExecutionRolePolicy

__all__: list[str] = ['AWS_NO_VALUE', 'AdditionalExecutionPolicy', 'AdditionalPolicyProvidedCondition', 'Equals', 'If', 'LambdaTimeout', 'NUMBER', 'Not', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'STRING', 'Sub', 'Template', 'TemplateCondition', 'Transform', 'TransformExecutionRole', 'TransformExecutionRoleAllowStatement0', 'TransformExecutionRoleAllowStatement0_1', 'TransformExecutionRoleAssumeRolePolicyDocument', 'TransformExecutionRolePolicies0PolicyDocument', 'TransformExecutionRolePolicy', 'TransformFunction', 'TransformFunctionCode', 'TransformFunctionPermissions', 'cloudformation', 'cloudformation_dataclass', 'get_att', 'iam', 'lambda_', 'ref', 'setup_resources']
