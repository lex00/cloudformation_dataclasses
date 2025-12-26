"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import AWS_REGION, Select

from .network import InternetGateway as InternetGateway
from .network import PrivateSubnet1DefaultRoute as PrivateSubnet1DefaultRoute
from .network import PrivateSubnet1RouteTable as PrivateSubnet1RouteTable
from .network import PrivateSubnet1RouteTableAssociation as PrivateSubnet1RouteTableAssociation
from .network import PrivateSubnet1Subnet as PrivateSubnet1Subnet
from .network import PrivateSubnet2DefaultRoute as PrivateSubnet2DefaultRoute
from .network import PrivateSubnet2RouteTable as PrivateSubnet2RouteTable
from .network import PrivateSubnet2RouteTableAssociation as PrivateSubnet2RouteTableAssociation
from .network import PrivateSubnet2Subnet as PrivateSubnet2Subnet
from .network import PublicSubnet1 as PublicSubnet1
from .network import PublicSubnet1DefaultRoute as PublicSubnet1DefaultRoute
from .network import PublicSubnet1EIP as PublicSubnet1EIP
from .network import PublicSubnet1NATGateway as PublicSubnet1NATGateway
from .network import PublicSubnet1RouteTable as PublicSubnet1RouteTable
from .network import PublicSubnet1RouteTableAssociation as PublicSubnet1RouteTableAssociation
from .network import PublicSubnet2 as PublicSubnet2
from .network import PublicSubnet2DefaultRoute as PublicSubnet2DefaultRoute
from .network import PublicSubnet2EIP as PublicSubnet2EIP
from .network import PublicSubnet2NATGateway as PublicSubnet2NATGateway
from .network import PublicSubnet2RouteTable as PublicSubnet2RouteTable
from .network import PublicSubnet2RouteTableAssociation as PublicSubnet2RouteTableAssociation
from .network import VPC as VPC
from .network import VPCGW as VPCGW

__all__: list[str] = ['AWS_REGION', 'InternetGateway', 'PrivateSubnet1DefaultRoute', 'PrivateSubnet1RouteTable', 'PrivateSubnet1RouteTableAssociation', 'PrivateSubnet1Subnet', 'PrivateSubnet2DefaultRoute', 'PrivateSubnet2RouteTable', 'PrivateSubnet2RouteTableAssociation', 'PrivateSubnet2Subnet', 'PublicSubnet1', 'PublicSubnet1DefaultRoute', 'PublicSubnet1EIP', 'PublicSubnet1NATGateway', 'PublicSubnet1RouteTable', 'PublicSubnet1RouteTableAssociation', 'PublicSubnet2', 'PublicSubnet2DefaultRoute', 'PublicSubnet2EIP', 'PublicSubnet2NATGateway', 'PublicSubnet2RouteTable', 'PublicSubnet2RouteTableAssociation', 'Select', 'Template', 'VPC', 'VPCGW', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
