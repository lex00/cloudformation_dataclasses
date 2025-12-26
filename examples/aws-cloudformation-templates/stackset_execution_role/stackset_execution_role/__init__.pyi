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
from cloudformation_dataclasses.aws import iam
from cloudformation_dataclasses.intrinsics import Sub

from .outputs import ExecutionRoleArnOutput as ExecutionRoleArnOutput
from .params import AdministrationAccountId as AdministrationAccountId
from .security import AWSCloudFormationStackSetExecutionRole as AWSCloudFormationStackSetExecutionRole
from .security import AWSCloudFormationStackSetExecutionRoleAllowStatement0 as AWSCloudFormationStackSetExecutionRoleAllowStatement0
from .security import AWSCloudFormationStackSetExecutionRoleAllowStatement0_1 as AWSCloudFormationStackSetExecutionRoleAllowStatement0_1
from .security import AWSCloudFormationStackSetExecutionRoleAllowStatement1 as AWSCloudFormationStackSetExecutionRoleAllowStatement1
from .security import AWSCloudFormationStackSetExecutionRoleAllowStatement2 as AWSCloudFormationStackSetExecutionRoleAllowStatement2
from .security import AWSCloudFormationStackSetExecutionRoleAllowStatement3 as AWSCloudFormationStackSetExecutionRoleAllowStatement3
from .security import AWSCloudFormationStackSetExecutionRoleAllowStatement4 as AWSCloudFormationStackSetExecutionRoleAllowStatement4
from .security import AWSCloudFormationStackSetExecutionRoleAssumeRolePolicyDocument as AWSCloudFormationStackSetExecutionRoleAssumeRolePolicyDocument
from .security import AWSCloudFormationStackSetExecutionRolePolicies0PolicyDocument as AWSCloudFormationStackSetExecutionRolePolicies0PolicyDocument
from .security import AWSCloudFormationStackSetExecutionRolePolicy as AWSCloudFormationStackSetExecutionRolePolicy

__all__: list[str] = ['AWSCloudFormationStackSetExecutionRole', 'AWSCloudFormationStackSetExecutionRoleAllowStatement0', 'AWSCloudFormationStackSetExecutionRoleAllowStatement0_1', 'AWSCloudFormationStackSetExecutionRoleAllowStatement1', 'AWSCloudFormationStackSetExecutionRoleAllowStatement2', 'AWSCloudFormationStackSetExecutionRoleAllowStatement3', 'AWSCloudFormationStackSetExecutionRoleAllowStatement4', 'AWSCloudFormationStackSetExecutionRoleAssumeRolePolicyDocument', 'AWSCloudFormationStackSetExecutionRolePolicies0PolicyDocument', 'AWSCloudFormationStackSetExecutionRolePolicy', 'AdministrationAccountId', 'ExecutionRoleArnOutput', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'STRING', 'Sub', 'Template', 'cloudformation_dataclass', 'get_att', 'iam', 'ref', 'setup_resources']
