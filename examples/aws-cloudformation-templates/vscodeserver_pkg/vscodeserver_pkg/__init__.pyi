"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
    Output,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.aws.ec2 import (
    EIP,
    NatGateway,
    NetworkAcl,
    NetworkAclEntry,
    RouteTable,
    Subnet,
    SubnetNetworkAclAssociation,
    SubnetRouteTableAssociation,
    VPCGatewayAttachment,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_STACK_NAME,
    FindInMap,
    GetAZs,
    Join,
    Select,
    Sub,
)

from .compute import InboundHTTPPublicNetworkAclEntry as InboundHTTPPublicNetworkAclEntry
from .compute import InboundHTTPPublicNetworkAclEntryPortRange as InboundHTTPPublicNetworkAclEntryPortRange
from .compute import OutboundPublicNetworkAclEntry as OutboundPublicNetworkAclEntry
from .compute import OutboundPublicNetworkAclEntryPortRange as OutboundPublicNetworkAclEntryPortRange
from .compute import PublicSubnetNetworkAclAssociation0 as PublicSubnetNetworkAclAssociation0
from .compute import PublicSubnetNetworkAclAssociation1 as PublicSubnetNetworkAclAssociation1
from .network import ElasticIP0 as ElasticIP0
from .network import ElasticIP1 as ElasticIP1
from .network import GatewayToInternet as GatewayToInternet
from .network import InternetGateway as InternetGateway
from .network import InternetGatewayAssociationParameter as InternetGatewayAssociationParameter
from .network import InternetGatewayAssociationParameter1 as InternetGatewayAssociationParameter1
from .network import InternetGatewayAssociationParameter2 as InternetGatewayAssociationParameter2
from .network import NATGateway0 as NATGateway0
from .network import NATGateway1 as NATGateway1
from .network import PrivateRouteTable0 as PrivateRouteTable0
from .network import PrivateRouteTable0AssociationParameter as PrivateRouteTable0AssociationParameter
from .network import PrivateRouteTable1 as PrivateRouteTable1
from .network import PrivateRouteTable1AssociationParameter as PrivateRouteTable1AssociationParameter
from .network import PrivateRouteToInternet0 as PrivateRouteToInternet0
from .network import PrivateRouteToInternet1 as PrivateRouteToInternet1
from .network import PrivateSubnet0 as PrivateSubnet0
from .network import PrivateSubnet0AssociationParameter as PrivateSubnet0AssociationParameter
from .network import PrivateSubnet0AssociationParameter1 as PrivateSubnet0AssociationParameter1
from .network import PrivateSubnet0AssociationParameter2 as PrivateSubnet0AssociationParameter2
from .network import PrivateSubnet1 as PrivateSubnet1
from .network import PrivateSubnet1AssociationParameter as PrivateSubnet1AssociationParameter
from .network import PrivateSubnet1AssociationParameter1 as PrivateSubnet1AssociationParameter1
from .network import PrivateSubnet1AssociationParameter2 as PrivateSubnet1AssociationParameter2
from .network import PrivateSubnetRouteTableAssociation0 as PrivateSubnetRouteTableAssociation0
from .network import PrivateSubnetRouteTableAssociation1 as PrivateSubnetRouteTableAssociation1
from .network import PublicNetworkAcl as PublicNetworkAcl
from .network import PublicNetworkAclAssociationParameter as PublicNetworkAclAssociationParameter
from .network import PublicNetworkAclAssociationParameter1 as PublicNetworkAclAssociationParameter1
from .network import PublicNetworkAclAssociationParameter2 as PublicNetworkAclAssociationParameter2
from .network import PublicRoute as PublicRoute
from .network import PublicRouteTable as PublicRouteTable
from .network import PublicRouteTableAssociationParameter as PublicRouteTableAssociationParameter
from .network import PublicRouteTableAssociationParameter1 as PublicRouteTableAssociationParameter1
from .network import PublicRouteTableAssociationParameter2 as PublicRouteTableAssociationParameter2
from .network import PublicSubnet0 as PublicSubnet0
from .network import PublicSubnet0AssociationParameter as PublicSubnet0AssociationParameter
from .network import PublicSubnet0AssociationParameter1 as PublicSubnet0AssociationParameter1
from .network import PublicSubnet0AssociationParameter2 as PublicSubnet0AssociationParameter2
from .network import PublicSubnet1 as PublicSubnet1
from .network import PublicSubnet1AssociationParameter as PublicSubnet1AssociationParameter
from .network import PublicSubnet1AssociationParameter1 as PublicSubnet1AssociationParameter1
from .network import PublicSubnet1AssociationParameter2 as PublicSubnet1AssociationParameter2
from .network import PublicSubnetRouteTableAssociation0 as PublicSubnetRouteTableAssociation0
from .network import PublicSubnetRouteTableAssociation1 as PublicSubnetRouteTableAssociation1
from .network import VPC as VPC
from .network import VPCAssociationParameter as VPCAssociationParameter
from .network import VPCAssociationParameter1 as VPCAssociationParameter1
from .network import VPCAssociationParameter2 as VPCAssociationParameter2
from .outputs import DefaultSecurityGroupOutput as DefaultSecurityGroupOutput
from .outputs import PrivateSubnet0Output as PrivateSubnet0Output
from .outputs import PrivateSubnet1Output as PrivateSubnet1Output
from .outputs import PublicSubnet0Output as PublicSubnet0Output
from .outputs import PublicSubnet1Output as PublicSubnet1Output
from .outputs import VPCIdOutput as VPCIdOutput
from .params import SubnetConfigMapping as SubnetConfigMapping
from .params import VPCName as VPCName

__all__: list[str] = ['AWS_STACK_NAME', 'DefaultSecurityGroupOutput', 'EIP', 'ElasticIP0', 'ElasticIP1', 'FindInMap', 'GatewayToInternet', 'GetAZs', 'InboundHTTPPublicNetworkAclEntry', 'InboundHTTPPublicNetworkAclEntryPortRange', 'InternetGateway', 'InternetGatewayAssociationParameter', 'InternetGatewayAssociationParameter1', 'InternetGatewayAssociationParameter2', 'Join', 'Mapping', 'NATGateway0', 'NATGateway1', 'NatGateway', 'NetworkAcl', 'NetworkAclEntry', 'OutboundPublicNetworkAclEntry', 'OutboundPublicNetworkAclEntryPortRange', 'Output', 'Parameter', 'PrivateRouteTable0', 'PrivateRouteTable0AssociationParameter', 'PrivateRouteTable1', 'PrivateRouteTable1AssociationParameter', 'PrivateRouteToInternet0', 'PrivateRouteToInternet1', 'PrivateSubnet0', 'PrivateSubnet0AssociationParameter', 'PrivateSubnet0AssociationParameter1', 'PrivateSubnet0AssociationParameter2', 'PrivateSubnet0Output', 'PrivateSubnet1', 'PrivateSubnet1AssociationParameter', 'PrivateSubnet1AssociationParameter1', 'PrivateSubnet1AssociationParameter2', 'PrivateSubnet1Output', 'PrivateSubnetRouteTableAssociation0', 'PrivateSubnetRouteTableAssociation1', 'PublicNetworkAcl', 'PublicNetworkAclAssociationParameter', 'PublicNetworkAclAssociationParameter1', 'PublicNetworkAclAssociationParameter2', 'PublicRoute', 'PublicRouteTable', 'PublicRouteTableAssociationParameter', 'PublicRouteTableAssociationParameter1', 'PublicRouteTableAssociationParameter2', 'PublicSubnet0', 'PublicSubnet0AssociationParameter', 'PublicSubnet0AssociationParameter1', 'PublicSubnet0AssociationParameter2', 'PublicSubnet0Output', 'PublicSubnet1', 'PublicSubnet1AssociationParameter', 'PublicSubnet1AssociationParameter1', 'PublicSubnet1AssociationParameter2', 'PublicSubnet1Output', 'PublicSubnetNetworkAclAssociation0', 'PublicSubnetNetworkAclAssociation1', 'PublicSubnetRouteTableAssociation0', 'PublicSubnetRouteTableAssociation1', 'RouteTable', 'STRING', 'Select', 'Sub', 'Subnet', 'SubnetConfigMapping', 'SubnetNetworkAclAssociation', 'SubnetRouteTableAssociation', 'Template', 'VPC', 'VPCAssociationParameter', 'VPCAssociationParameter1', 'VPCAssociationParameter2', 'VPCGatewayAttachment', 'VPCIdOutput', 'VPCName', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
