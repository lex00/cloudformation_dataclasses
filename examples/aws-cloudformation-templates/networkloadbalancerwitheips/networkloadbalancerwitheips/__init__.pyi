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
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2, elasticloadbalancingv2
from cloudformation_dataclasses.intrinsics import Select

from .network import EIP1 as EIP1
from .network import EIP2 as EIP2
from .network import FirstEIP as FirstEIP
from .network import Listener as Listener
from .network import ListenerAction as ListenerAction
from .network import SecondEIP as SecondEIP
from .network import TargetGroup as TargetGroup
from .network import TargetGroupLoadBalancerAttribute as TargetGroupLoadBalancerAttribute
from .network import loadBalancer as loadBalancer
from .network import loadBalancerSubnetMapping as loadBalancerSubnetMapping
from .network import loadBalancerSubnetMapping1 as loadBalancerSubnetMapping1
from .params import ELBIpAddressType as ELBIpAddressType
from .params import ELBType as ELBType
from .params import Subnet1 as Subnet1
from .params import Subnet2 as Subnet2
from .params import VPC as VPC

__all__: list[str] = ['EIP1', 'EIP2', 'ELBIpAddressType', 'ELBType', 'FirstEIP', 'Listener', 'ListenerAction', 'Parameter', 'ParameterType', 'STRING', 'SecondEIP', 'Select', 'Subnet1', 'Subnet2', 'TargetGroup', 'TargetGroupLoadBalancerAttribute', 'Template', 'VPC', 'cloudformation_dataclass', 'ec2', 'elasticloadbalancingv2', 'get_att', 'loadBalancer', 'loadBalancerSubnetMapping', 'loadBalancerSubnetMapping1', 'ref', 'setup_resources']
