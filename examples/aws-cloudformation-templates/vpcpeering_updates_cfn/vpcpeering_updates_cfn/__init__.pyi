"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
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
    Condition,
    Equals,
    Or,
    Select,
    Split,
    Sub,
)
from .params import *  # noqa: F403, F401

from .compute import PeerIngressRule1 as PeerIngressRule1
from .compute import PeerIngressRule2 as PeerIngressRule2
from .compute import PeerIngressRule3 as PeerIngressRule3
from .compute import PeerIngressRule4 as PeerIngressRule4
from .compute import PeerIngressRule5 as PeerIngressRule5
from .compute import PeerIngressRule6 as PeerIngressRule6
from .network import PeerRoute1 as PeerRoute1
from .network import PeerRoute2 as PeerRoute2
from .network import PeerRoute3 as PeerRoute3
from .network import PeerRoute4 as PeerRoute4
from .network import PeerRoute5 as PeerRoute5
from .network import PeerRoute6 as PeerRoute6
from .params import NumberOfRouteTables as NumberOfRouteTables
from .params import NumberOfSecurityGroups as NumberOfSecurityGroups
from .params import PeerName as PeerName
from .params import PeerVPCCIDR as PeerVPCCIDR
from .params import RouteTableIds as RouteTableIds
from .params import SecurityGroupIds as SecurityGroupIds
from .params import VPCPeeringConnectionId as VPCPeeringConnectionId
from .params import _2RouteTableConditionCondition as _2RouteTableConditionCondition
from .params import _2SecurityGroupConditionCondition as _2SecurityGroupConditionCondition
from .params import _3RouteTableConditionCondition as _3RouteTableConditionCondition
from .params import _3SecurityGroupConditionCondition as _3SecurityGroupConditionCondition
from .params import _4RouteTableConditionCondition as _4RouteTableConditionCondition
from .params import _4SecurityGroupConditionCondition as _4SecurityGroupConditionCondition
from .params import _5RouteTableConditionCondition as _5RouteTableConditionCondition
from .params import _5SecurityGroupConditionCondition as _5SecurityGroupConditionCondition
from .params import _6RouteTableConditionCondition as _6RouteTableConditionCondition
from .params import _6SecurityGroupConditionCondition as _6SecurityGroupConditionCondition

__all__: list[str] = ['Condition', 'Equals', 'NumberOfRouteTables', 'NumberOfSecurityGroups', 'Or', 'Parameter', 'ParameterType', 'PeerIngressRule1', 'PeerIngressRule2', 'PeerIngressRule3', 'PeerIngressRule4', 'PeerIngressRule5', 'PeerIngressRule6', 'PeerName', 'PeerRoute1', 'PeerRoute2', 'PeerRoute3', 'PeerRoute4', 'PeerRoute5', 'PeerRoute6', 'PeerVPCCIDR', 'RouteTableIds', 'STRING', 'SecurityGroupIds', 'Select', 'Split', 'Sub', 'Template', 'TemplateCondition', 'VPCPeeringConnectionId', '_2RouteTableConditionCondition', '_2SecurityGroupConditionCondition', '_3RouteTableConditionCondition', '_3SecurityGroupConditionCondition', '_4RouteTableConditionCondition', '_4SecurityGroupConditionCondition', '_5RouteTableConditionCondition', '_5SecurityGroupConditionCondition', '_6RouteTableConditionCondition', '_6SecurityGroupConditionCondition', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
