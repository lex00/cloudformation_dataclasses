"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
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
from cloudformation_dataclasses.aws import ec2, eks, iam
from cloudformation_dataclasses.aws.ec2.instance import AssociationParameter
from cloudformation_dataclasses.intrinsics import (
    AWS_ACCOUNT_ID,
    AWS_PARTITION,
    AWS_REGION,
    FindInMap,
    GetAZs,
    Select,
    Sub,
)
from .params import *  # noqa: F403, F401

from .compute import ControlPlane as ControlPlane
from .compute import ControlPlaneResourcesVpcConfig as ControlPlaneResourcesVpcConfig
from .compute import ControlPlaneSecurityGroupIngress as ControlPlaneSecurityGroupIngress
from .compute import LaunchTemplate as LaunchTemplate
from .compute import LaunchTemplateBlockDeviceMapping as LaunchTemplateBlockDeviceMapping
from .compute import LaunchTemplateEbs as LaunchTemplateEbs
from .compute import LaunchTemplateLaunchTemplateData as LaunchTemplateLaunchTemplateData
from .compute import LaunchTemplateMetadataOptions as LaunchTemplateMetadataOptions
from .compute import LaunchTemplateTagSpecification as LaunchTemplateTagSpecification
from .compute import LaunchTemplateTagSpecification1 as LaunchTemplateTagSpecification1
from .compute import LaunchTemplateTagSpecification2 as LaunchTemplateTagSpecification2
from .compute import ManagedNodeGroup as ManagedNodeGroup
from .compute import ManagedNodeGroupScalingConfig as ManagedNodeGroupScalingConfig
from .compute import ManagedNodeGroupSsoIdentity as ManagedNodeGroupSsoIdentity
from .network import AttachGateway as AttachGateway
from .network import ControlPlaneSecurityGroup as ControlPlaneSecurityGroup
from .network import EIP1 as EIP1
from .network import EIP2 as EIP2
from .network import EIP3 as EIP3
from .network import InternetGateway as InternetGateway
from .network import InternetGatewayAssociationParameter as InternetGatewayAssociationParameter
from .network import NATGateway1 as NATGateway1
from .network import NATGateway1AssociationParameter as NATGateway1AssociationParameter
from .network import NATGateway2 as NATGateway2
from .network import NATGateway2AssociationParameter as NATGateway2AssociationParameter
from .network import NATGateway3 as NATGateway3
from .network import NATGateway3AssociationParameter as NATGateway3AssociationParameter
from .network import PrivateRoute1 as PrivateRoute1
from .network import PrivateRoute2 as PrivateRoute2
from .network import PrivateRoute3 as PrivateRoute3
from .network import PrivateRouteTable1 as PrivateRouteTable1
from .network import PrivateRouteTable1AssociationParameter as PrivateRouteTable1AssociationParameter
from .network import PrivateRouteTable2 as PrivateRouteTable2
from .network import PrivateRouteTable2AssociationParameter as PrivateRouteTable2AssociationParameter
from .network import PrivateRouteTable3 as PrivateRouteTable3
from .network import PrivateRouteTable3AssociationParameter as PrivateRouteTable3AssociationParameter
from .network import PrivateRouteTableAssociation1 as PrivateRouteTableAssociation1
from .network import PrivateRouteTableAssociation2 as PrivateRouteTableAssociation2
from .network import PrivateRouteTableAssociation3 as PrivateRouteTableAssociation3
from .network import PrivateSubnet1 as PrivateSubnet1
from .network import PrivateSubnet1AssociationParameter as PrivateSubnet1AssociationParameter
from .network import PrivateSubnet2 as PrivateSubnet2
from .network import PrivateSubnet2AssociationParameter as PrivateSubnet2AssociationParameter
from .network import PrivateSubnet3 as PrivateSubnet3
from .network import PrivateSubnet3AssociationParameter as PrivateSubnet3AssociationParameter
from .network import PublicRouteTable as PublicRouteTable
from .network import PublicRouteTableAssociation1 as PublicRouteTableAssociation1
from .network import PublicRouteTableAssociation2 as PublicRouteTableAssociation2
from .network import PublicRouteTableAssociation3 as PublicRouteTableAssociation3
from .network import PublicRouteTableAssociationParameter as PublicRouteTableAssociationParameter
from .network import PublicSubnet1 as PublicSubnet1
from .network import PublicSubnet1AssociationParameter as PublicSubnet1AssociationParameter
from .network import PublicSubnet1AssociationParameter1 as PublicSubnet1AssociationParameter1
from .network import PublicSubnet2 as PublicSubnet2
from .network import PublicSubnet2AssociationParameter as PublicSubnet2AssociationParameter
from .network import PublicSubnet2AssociationParameter1 as PublicSubnet2AssociationParameter1
from .network import PublicSubnet3 as PublicSubnet3
from .network import PublicSubnet3AssociationParameter as PublicSubnet3AssociationParameter
from .network import PublicSubnet3AssociationParameter1 as PublicSubnet3AssociationParameter1
from .network import RouteInternetGateway as RouteInternetGateway
from .network import VPC as VPC
from .network import VPCAssociationParameter as VPCAssociationParameter
from .params import EKSClusterVersion as EKSClusterVersion
from .params import NodeGroupInstanceTypes as NodeGroupInstanceTypes
from .params import PrivateCidrBlock1 as PrivateCidrBlock1
from .params import PrivateCidrBlock2 as PrivateCidrBlock2
from .params import PrivateCidrBlock3 as PrivateCidrBlock3
from .params import PublicCidrBlock1 as PublicCidrBlock1
from .params import PublicCidrBlock2 as PublicCidrBlock2
from .params import PublicCidrBlock3 as PublicCidrBlock3
from .params import ServicePrincipalPartitionMapMapping as ServicePrincipalPartitionMapMapping
from .params import VPCCidrBlock as VPCCidrBlock
from .security import EKSClusterRole as EKSClusterRole
from .security import EKSClusterRoleAllowStatement0 as EKSClusterRoleAllowStatement0
from .security import EKSClusterRoleAssumeRolePolicyDocument as EKSClusterRoleAssumeRolePolicyDocument
from .security import NodeInstanceRole as NodeInstanceRole
from .security import NodeInstanceRoleAllowStatement0 as NodeInstanceRoleAllowStatement0
from .security import NodeInstanceRoleAssumeRolePolicyDocument as NodeInstanceRoleAssumeRolePolicyDocument

__all__: list[str] = ['AWS_ACCOUNT_ID', 'AWS_PARTITION', 'AWS_REGION', 'AssociationParameter', 'AttachGateway', 'ControlPlane', 'ControlPlaneResourcesVpcConfig', 'ControlPlaneSecurityGroup', 'ControlPlaneSecurityGroupIngress', 'EIP1', 'EIP2', 'EIP3', 'EKSClusterRole', 'EKSClusterRoleAllowStatement0', 'EKSClusterRoleAssumeRolePolicyDocument', 'EKSClusterVersion', 'FindInMap', 'GetAZs', 'InternetGateway', 'InternetGatewayAssociationParameter', 'LaunchTemplate', 'LaunchTemplateBlockDeviceMapping', 'LaunchTemplateEbs', 'LaunchTemplateLaunchTemplateData', 'LaunchTemplateMetadataOptions', 'LaunchTemplateTagSpecification', 'LaunchTemplateTagSpecification1', 'LaunchTemplateTagSpecification2', 'ManagedNodeGroup', 'ManagedNodeGroupScalingConfig', 'ManagedNodeGroupSsoIdentity', 'Mapping', 'NATGateway1', 'NATGateway1AssociationParameter', 'NATGateway2', 'NATGateway2AssociationParameter', 'NATGateway3', 'NATGateway3AssociationParameter', 'NodeGroupInstanceTypes', 'NodeInstanceRole', 'NodeInstanceRoleAllowStatement0', 'NodeInstanceRoleAssumeRolePolicyDocument', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PrivateCidrBlock1', 'PrivateCidrBlock2', 'PrivateCidrBlock3', 'PrivateRoute1', 'PrivateRoute2', 'PrivateRoute3', 'PrivateRouteTable1', 'PrivateRouteTable1AssociationParameter', 'PrivateRouteTable2', 'PrivateRouteTable2AssociationParameter', 'PrivateRouteTable3', 'PrivateRouteTable3AssociationParameter', 'PrivateRouteTableAssociation1', 'PrivateRouteTableAssociation2', 'PrivateRouteTableAssociation3', 'PrivateSubnet1', 'PrivateSubnet1AssociationParameter', 'PrivateSubnet2', 'PrivateSubnet2AssociationParameter', 'PrivateSubnet3', 'PrivateSubnet3AssociationParameter', 'PublicCidrBlock1', 'PublicCidrBlock2', 'PublicCidrBlock3', 'PublicRouteTable', 'PublicRouteTableAssociation1', 'PublicRouteTableAssociation2', 'PublicRouteTableAssociation3', 'PublicRouteTableAssociationParameter', 'PublicSubnet1', 'PublicSubnet1AssociationParameter', 'PublicSubnet1AssociationParameter1', 'PublicSubnet2', 'PublicSubnet2AssociationParameter', 'PublicSubnet2AssociationParameter1', 'PublicSubnet3', 'PublicSubnet3AssociationParameter', 'PublicSubnet3AssociationParameter1', 'RouteInternetGateway', 'STRING', 'Select', 'ServicePrincipalPartitionMapMapping', 'Sub', 'Template', 'VPC', 'VPCAssociationParameter', 'VPCCidrBlock', 'cloudformation_dataclass', 'ec2', 'eks', 'get_att', 'iam', 'ref', 'setup_resources']
