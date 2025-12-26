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
from cloudformation_dataclasses.intrinsics import AWS_STACK_NAME, Split

from .outputs import PeerRoleARNOutput as PeerRoleARNOutput
from .params import PeerOwnerIds as PeerOwnerIds
from .security import PeerRole as PeerRole
from .security import PeerRoleAllowStatement0 as PeerRoleAllowStatement0
from .security import PeerRoleAllowStatement0_1 as PeerRoleAllowStatement0_1
from .security import PeerRoleAssumeRolePolicyDocument as PeerRoleAssumeRolePolicyDocument
from .security import PeerRolePolicies0PolicyDocument as PeerRolePolicies0PolicyDocument
from .security import PeerRolePolicy as PeerRolePolicy

__all__: list[str] = ['AWS_STACK_NAME', 'Output', 'Parameter', 'PeerOwnerIds', 'PeerRole', 'PeerRoleARNOutput', 'PeerRoleAllowStatement0', 'PeerRoleAllowStatement0_1', 'PeerRoleAssumeRolePolicyDocument', 'PeerRolePolicies0PolicyDocument', 'PeerRolePolicy', 'PolicyDocument', 'PolicyStatement', 'STRING', 'Split', 'Template', 'cloudformation_dataclass', 'get_att', 'iam', 'ref', 'setup_resources']
