"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import GetAZs, Join, Select
from . import stack

from .stack.network import InternetGateway as InternetGateway
from .stack.network import InternetGatewayAttachment as InternetGatewayAttachment
from .stack.network import NatEip1 as NatEip1
from .stack.network import NatEip2 as NatEip2
from .stack.network import NatEip3 as NatEip3
from .stack.network import NatGateway1 as NatGateway1
from .stack.network import NatGateway2 as NatGateway2
from .stack.network import NatGateway3 as NatGateway3
from .stack.network import PrivateRoute1 as PrivateRoute1
from .stack.network import PrivateRoute2 as PrivateRoute2
from .stack.network import PrivateRoute3 as PrivateRoute3
from .stack.network import PrivateRouteTable1 as PrivateRouteTable1
from .stack.network import PrivateRouteTable2 as PrivateRouteTable2
from .stack.network import PrivateRouteTable3 as PrivateRouteTable3
from .stack.network import PrivateSubnet1 as PrivateSubnet1
from .stack.network import PrivateSubnet1RouteTableAssociation as PrivateSubnet1RouteTableAssociation
from .stack.network import PrivateSubnet2 as PrivateSubnet2
from .stack.network import PrivateSubnet2RouteTableAssociation as PrivateSubnet2RouteTableAssociation
from .stack.network import PrivateSubnet3 as PrivateSubnet3
from .stack.network import PrivateSubnet3RouteTableAssociation as PrivateSubnet3RouteTableAssociation
from .stack.network import PublicRoute as PublicRoute
from .stack.network import PublicRouteTable as PublicRouteTable
from .stack.network import PublicSubnet1 as PublicSubnet1
from .stack.network import PublicSubnet1RouteTableAssociation as PublicSubnet1RouteTableAssociation
from .stack.network import PublicSubnet2 as PublicSubnet2
from .stack.network import PublicSubnet2RouteTableAssociation as PublicSubnet2RouteTableAssociation
from .stack.network import PublicSubnet3 as PublicSubnet3
from .stack.network import PublicSubnet3RouteTableAssociation as PublicSubnet3RouteTableAssociation
from .stack.network import Vpc as Vpc

__all__: list[str] = ['GetAZs', 'InternetGateway', 'InternetGatewayAttachment', 'Join', 'NatEip1', 'NatEip2', 'NatEip3', 'NatGateway1', 'NatGateway2', 'NatGateway3', 'Output', 'PrivateRoute1', 'PrivateRoute2', 'PrivateRoute3', 'PrivateRouteTable1', 'PrivateRouteTable2', 'PrivateRouteTable3', 'PrivateSubnet1', 'PrivateSubnet1RouteTableAssociation', 'PrivateSubnet2', 'PrivateSubnet2RouteTableAssociation', 'PrivateSubnet3', 'PrivateSubnet3RouteTableAssociation', 'PublicRoute', 'PublicRouteTable', 'PublicSubnet1', 'PublicSubnet1RouteTableAssociation', 'PublicSubnet2', 'PublicSubnet2RouteTableAssociation', 'PublicSubnet3', 'PublicSubnet3RouteTableAssociation', 'Select', 'Template', 'Vpc', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'stack']
