"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    PolicyDocument,
    PolicyStatement,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iam, lambda_
from cloudformation_dataclasses.aws.cloudformation import Macro

from .compute import TransformFunction as TransformFunction
from .compute import TransformFunctionCode as TransformFunctionCode
from .compute import TransformFunctionPermissions as TransformFunctionPermissions
from .infra import Transform as Transform
from .security import TransformExecutionRole as TransformExecutionRole
from .security import TransformExecutionRoleAllowStatement0 as TransformExecutionRoleAllowStatement0
from .security import TransformExecutionRoleAllowStatement0_1 as TransformExecutionRoleAllowStatement0_1
from .security import TransformExecutionRoleAssumeRolePolicyDocument as TransformExecutionRoleAssumeRolePolicyDocument
from .security import TransformExecutionRolePolicies0PolicyDocument as TransformExecutionRolePolicies0PolicyDocument
from .security import TransformExecutionRolePolicy as TransformExecutionRolePolicy

__all__: list[str] = ['Macro', 'PolicyDocument', 'PolicyStatement', 'Template', 'Transform', 'TransformExecutionRole', 'TransformExecutionRoleAllowStatement0', 'TransformExecutionRoleAllowStatement0_1', 'TransformExecutionRoleAssumeRolePolicyDocument', 'TransformExecutionRolePolicies0PolicyDocument', 'TransformExecutionRolePolicy', 'TransformFunction', 'TransformFunctionCode', 'TransformFunctionPermissions', 'cloudformation_dataclass', 'get_att', 'iam', 'lambda_', 'ref', 'setup_resources']
