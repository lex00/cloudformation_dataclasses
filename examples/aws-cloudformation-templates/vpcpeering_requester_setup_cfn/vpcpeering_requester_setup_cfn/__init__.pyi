"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    Equals,
    If,
    Not,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import VPCPeeringConnection as VPCPeeringConnection
from .compute import VPCPeeringConnectionAssociationParameter as VPCPeeringConnectionAssociationParameter
from .outputs import VPCPeeringConnectionIdOutput as VPCPeeringConnectionIdOutput
from .params import PeerName as PeerName
from .params import PeerOwnerId as PeerOwnerId
from .params import PeerRoleARN as PeerRoleARN
from .params import PeerRoleConditionCondition as PeerRoleConditionCondition
from .params import PeerVPCID as PeerVPCID
from .params import VPCID as VPCID

__all__: list[str] = ['AWS_NO_VALUE', 'Equals', 'If', 'Not', 'Output', 'Parameter', 'ParameterType', 'PeerName', 'PeerOwnerId', 'PeerRoleARN', 'PeerRoleConditionCondition', 'PeerVPCID', 'STRING', 'Template', 'TemplateCondition', 'VPCID', 'VPCPeeringConnection', 'VPCPeeringConnectionAssociationParameter', 'VPCPeeringConnectionIdOutput', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
