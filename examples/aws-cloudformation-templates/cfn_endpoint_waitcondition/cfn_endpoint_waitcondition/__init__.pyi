"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    ParameterType,
    PolicyDocument,
    PolicyStatement,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation, ec2, iam
from cloudformation_dataclasses.intrinsics import (
    Base64,
    GetAZs,
    Join,
    Select,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import BastionInstance as BastionInstance
from .compute import BastionInstanceAssociationParameter as BastionInstanceAssociationParameter
from .compute import PrivateInstance as PrivateInstance
from .compute import PrivateInstanceAssociationParameter as PrivateInstanceAssociationParameter
from .infra import PrivateWaitCondition as PrivateWaitCondition
from .infra import PrivateWaitHandle as PrivateWaitHandle
from .network import BastionSG as BastionSG
from .network import BastionSGAssociationParameter as BastionSGAssociationParameter
from .network import BastionSGEgress as BastionSGEgress
from .network import CfnEndpoint as CfnEndpoint
from .network import DefaultPublicRoute as DefaultPublicRoute
from .network import EndpointSG as EndpointSG
from .network import EndpointSGAssociationParameter as EndpointSGAssociationParameter
from .network import EndpointSGEgress as EndpointSGEgress
from .network import InternetGateway as InternetGateway
from .network import InternetGatewayAssociationParameter as InternetGatewayAssociationParameter
from .network import InternetGatewayAttachment as InternetGatewayAttachment
from .network import PrivateRouteTable1 as PrivateRouteTable1
from .network import PrivateRouteTable1AssociationParameter as PrivateRouteTable1AssociationParameter
from .network import PrivateRouteTable2 as PrivateRouteTable2
from .network import PrivateRouteTable2AssociationParameter as PrivateRouteTable2AssociationParameter
from .network import PrivateSG as PrivateSG
from .network import PrivateSGAssociationParameter as PrivateSGAssociationParameter
from .network import PrivateSGIngress as PrivateSGIngress
from .network import PrivateSubnet1 as PrivateSubnet1
from .network import PrivateSubnet1AssociationParameter as PrivateSubnet1AssociationParameter
from .network import PrivateSubnet1RouteTableAssociation as PrivateSubnet1RouteTableAssociation
from .network import PrivateSubnet2 as PrivateSubnet2
from .network import PrivateSubnet2AssociationParameter as PrivateSubnet2AssociationParameter
from .network import PrivateSubnet2RouteTableAssociation as PrivateSubnet2RouteTableAssociation
from .network import PublicRouteTable as PublicRouteTable
from .network import PublicRouteTableAssociationParameter as PublicRouteTableAssociationParameter
from .network import PublicSubnet1 as PublicSubnet1
from .network import PublicSubnet1AssociationParameter as PublicSubnet1AssociationParameter
from .network import PublicSubnet1RouteTableAssociation as PublicSubnet1RouteTableAssociation
from .network import PublicSubnet2 as PublicSubnet2
from .network import PublicSubnet2AssociationParameter as PublicSubnet2AssociationParameter
from .network import PublicSubnet2RouteTableAssociation as PublicSubnet2RouteTableAssociation
from .network import S3Endpoint as S3Endpoint
from .network import S3EndpointAllowStatement0 as S3EndpointAllowStatement0
from .network import S3EndpointPolicyDocument as S3EndpointPolicyDocument
from .network import VPC as VPC
from .network import VPCAssociationParameter as VPCAssociationParameter
from .outputs import CfnEndpointOutput as CfnEndpointOutput
from .outputs import PrivateSubnetsOutput as PrivateSubnetsOutput
from .outputs import PublicSubnetsOutput as PublicSubnetsOutput
from .outputs import S3EndpointOutput as S3EndpointOutput
from .outputs import VPCOutput as VPCOutput
from .params import EnvironmentName as EnvironmentName
from .params import KeyName as KeyName
from .params import LinuxAMI as LinuxAMI
from .params import PrivateSubnet1CIDR as PrivateSubnet1CIDR
from .params import PrivateSubnet2CIDR as PrivateSubnet2CIDR
from .params import PublicSubnet1CIDR as PublicSubnet1CIDR
from .params import PublicSubnet2CIDR as PublicSubnet2CIDR
from .params import VpcCIDR as VpcCIDR
from .security import BastionProfile as BastionProfile
from .security import PrivateProfile as PrivateProfile
from .security import RootRole as RootRole
from .security import RootRoleAllowStatement0 as RootRoleAllowStatement0
from .security import RootRoleAllowStatement0_1 as RootRoleAllowStatement0_1
from .security import RootRoleAssumeRolePolicyDocument as RootRoleAssumeRolePolicyDocument
from .security import RootRolePolicies0PolicyDocument as RootRolePolicies0PolicyDocument
from .security import RootRolePolicy as RootRolePolicy

__all__: list[str] = ['Base64', 'BastionInstance', 'BastionInstanceAssociationParameter', 'BastionProfile', 'BastionSG', 'BastionSGAssociationParameter', 'BastionSGEgress', 'CfnEndpoint', 'CfnEndpointOutput', 'DefaultPublicRoute', 'EndpointSG', 'EndpointSGAssociationParameter', 'EndpointSGEgress', 'EnvironmentName', 'GetAZs', 'InternetGateway', 'InternetGatewayAssociationParameter', 'InternetGatewayAttachment', 'Join', 'KeyName', 'LinuxAMI', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'PrivateInstance', 'PrivateInstanceAssociationParameter', 'PrivateProfile', 'PrivateRouteTable1', 'PrivateRouteTable1AssociationParameter', 'PrivateRouteTable2', 'PrivateRouteTable2AssociationParameter', 'PrivateSG', 'PrivateSGAssociationParameter', 'PrivateSGIngress', 'PrivateSubnet1', 'PrivateSubnet1AssociationParameter', 'PrivateSubnet1CIDR', 'PrivateSubnet1RouteTableAssociation', 'PrivateSubnet2', 'PrivateSubnet2AssociationParameter', 'PrivateSubnet2CIDR', 'PrivateSubnet2RouteTableAssociation', 'PrivateSubnetsOutput', 'PrivateWaitCondition', 'PrivateWaitHandle', 'PublicRouteTable', 'PublicRouteTableAssociationParameter', 'PublicSubnet1', 'PublicSubnet1AssociationParameter', 'PublicSubnet1CIDR', 'PublicSubnet1RouteTableAssociation', 'PublicSubnet2', 'PublicSubnet2AssociationParameter', 'PublicSubnet2CIDR', 'PublicSubnet2RouteTableAssociation', 'PublicSubnetsOutput', 'RootRole', 'RootRoleAllowStatement0', 'RootRoleAllowStatement0_1', 'RootRoleAssumeRolePolicyDocument', 'RootRolePolicies0PolicyDocument', 'RootRolePolicy', 'S3Endpoint', 'S3EndpointAllowStatement0', 'S3EndpointOutput', 'S3EndpointPolicyDocument', 'STRING', 'Select', 'Sub', 'Template', 'VPC', 'VPCAssociationParameter', 'VPCOutput', 'VpcCIDR', 'cloudformation', 'cloudformation_dataclass', 'ec2', 'get_att', 'iam', 'ref', 'setup_resources']
