"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    PolicyDocument,
    PolicyStatement,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import iam
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .outputs import AdministrationRoleArnOutput as AdministrationRoleArnOutput
from .security import AWSCloudFormationStackSetAdministrationRole as AWSCloudFormationStackSetAdministrationRole
from .security import AWSCloudFormationStackSetAdministrationRoleAllowStatement0 as AWSCloudFormationStackSetAdministrationRoleAllowStatement0
from .security import AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1 as AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1
from .security import AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument as AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument
from .security import AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument as AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument
from .security import AWSCloudFormationStackSetAdministrationRolePolicy as AWSCloudFormationStackSetAdministrationRolePolicy

__all__: list[str] = ['AWSCloudFormationStackSetAdministrationRole', 'AWSCloudFormationStackSetAdministrationRoleAllowStatement0', 'AWSCloudFormationStackSetAdministrationRoleAllowStatement0_1', 'AWSCloudFormationStackSetAdministrationRoleAssumeRolePolicyDocument', 'AWSCloudFormationStackSetAdministrationRolePolicies0PolicyDocument', 'AWSCloudFormationStackSetAdministrationRolePolicy', 'AdministrationRoleArnOutput', 'Output', 'PolicyDocument', 'PolicyStatement', 'Template', 'cloudformation_dataclass', 'get_att', 'iam', 'ref', 'setup_resources']
