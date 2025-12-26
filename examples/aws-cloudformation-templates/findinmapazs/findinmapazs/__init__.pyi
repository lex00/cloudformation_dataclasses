"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import AWS_REGION, FindInMap, Select

from .network import DefaultPrivateRoute1 as DefaultPrivateRoute1
from .network import DefaultPrivateRoute2 as DefaultPrivateRoute2
from .network import DefaultPublicRoute as DefaultPublicRoute
from .network import InternetGateway as InternetGateway
from .network import InternetGatewayAttachment as InternetGatewayAttachment
from .network import NatGateway1 as NatGateway1
from .network import NatGateway1EIP as NatGateway1EIP
from .network import NatGateway2 as NatGateway2
from .network import NatGateway2EIP as NatGateway2EIP
from .network import NoIngressSecurityGroup as NoIngressSecurityGroup
from .network import PrivateRouteTable1 as PrivateRouteTable1
from .network import PrivateRouteTable2 as PrivateRouteTable2
from .network import PrivateSubnet1 as PrivateSubnet1
from .network import PrivateSubnet1RouteTableAssociation as PrivateSubnet1RouteTableAssociation
from .network import PrivateSubnet2 as PrivateSubnet2
from .network import PrivateSubnet2RouteTableAssociation as PrivateSubnet2RouteTableAssociation
from .network import PublicRouteTable as PublicRouteTable
from .network import PublicSubnet1 as PublicSubnet1
from .network import PublicSubnet1RouteTableAssociation as PublicSubnet1RouteTableAssociation
from .network import PublicSubnet2 as PublicSubnet2
from .network import PublicSubnet2RouteTableAssociation as PublicSubnet2RouteTableAssociation
from .network import VPC as VPC
from .params import PrivateSubnet1CIDR as PrivateSubnet1CIDR
from .params import PrivateSubnet2CIDR as PrivateSubnet2CIDR
from .params import PublicSubnet1CIDR as PublicSubnet1CIDR
from .params import PublicSubnet2CIDR as PublicSubnet2CIDR
from .params import RegionMapMapping as RegionMapMapping
from .params import VpcCIDR as VpcCIDR

__all__: list[str] = ['AWS_REGION', 'DefaultPrivateRoute1', 'DefaultPrivateRoute2', 'DefaultPublicRoute', 'FindInMap', 'InternetGateway', 'InternetGatewayAttachment', 'Mapping', 'NatGateway1', 'NatGateway1EIP', 'NatGateway2', 'NatGateway2EIP', 'NoIngressSecurityGroup', 'Parameter', 'PrivateRouteTable1', 'PrivateRouteTable2', 'PrivateSubnet1', 'PrivateSubnet1CIDR', 'PrivateSubnet1RouteTableAssociation', 'PrivateSubnet2', 'PrivateSubnet2CIDR', 'PrivateSubnet2RouteTableAssociation', 'PublicRouteTable', 'PublicSubnet1', 'PublicSubnet1CIDR', 'PublicSubnet1RouteTableAssociation', 'PublicSubnet2', 'PublicSubnet2CIDR', 'PublicSubnet2RouteTableAssociation', 'RegionMapMapping', 'STRING', 'Select', 'Template', 'VPC', 'VpcCIDR', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
