"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iam

from .params import PermissionBoundaryArn as PermissionBoundaryArn
from .security import ExecutionRoleBuilderMacroTestRole as ExecutionRoleBuilderMacroTestRole

__all__: list[str] = ['ExecutionRoleBuilderMacroTestRole', 'Parameter', 'PermissionBoundaryArn', 'STRING', 'Template', 'cloudformation_dataclass', 'get_att', 'iam', 'ref', 'setup_resources']
