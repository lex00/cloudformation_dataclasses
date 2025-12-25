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
from cloudformation_dataclasses.aws import cloudformation, ec2
from cloudformation_dataclasses.intrinsics import (
    Base64,
    GetAZs,
    Join,
    Select,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import PrivateInstance as PrivateInstance
from .compute import PrivateInstanceAssociationParameter as PrivateInstanceAssociationParameter
from .infra import PrivateWaitCondition as PrivateWaitCondition
from .infra import PrivateWaitHandle as PrivateWaitHandle
from .network import CfnEndpoint as CfnEndpoint
from .network import EndpointSG as EndpointSG
from .network import EndpointSGAssociationParameter as EndpointSGAssociationParameter
from .network import EndpointSGEgress as EndpointSGEgress
from .network import PrivateRouteTable1 as PrivateRouteTable1
from .network import PrivateRouteTable1AssociationParameter as PrivateRouteTable1AssociationParameter
from .network import PrivateRouteTable2 as PrivateRouteTable2
from .network import PrivateRouteTable2AssociationParameter as PrivateRouteTable2AssociationParameter
from .network import PrivateSG as PrivateSG
from .network import PrivateSGAssociationParameter as PrivateSGAssociationParameter
from .network import PrivateSGEgress as PrivateSGEgress
from .network import PrivateSubnet1 as PrivateSubnet1
from .network import PrivateSubnet1AssociationParameter as PrivateSubnet1AssociationParameter
from .network import PrivateSubnet1RouteTableAssociation as PrivateSubnet1RouteTableAssociation
from .network import PrivateSubnet2 as PrivateSubnet2
from .network import PrivateSubnet2AssociationParameter as PrivateSubnet2AssociationParameter
from .network import PrivateSubnet2RouteTableAssociation as PrivateSubnet2RouteTableAssociation
from .network import S3Endpoint as S3Endpoint
from .network import S3EndpointAllowStatement0 as S3EndpointAllowStatement0
from .network import S3EndpointPolicyDocument as S3EndpointPolicyDocument
from .network import VPC as VPC
from .network import VPCAssociationParameter as VPCAssociationParameter
from .outputs import CfnEndpointOutput as CfnEndpointOutput
from .outputs import PrivateSubnetsOutput as PrivateSubnetsOutput
from .outputs import S3EndpointOutput as S3EndpointOutput
from .outputs import VPCOutput as VPCOutput
from .params import EnvironmentName as EnvironmentName
from .params import LinuxAMI as LinuxAMI
from .params import PrivateSubnet1CIDR as PrivateSubnet1CIDR
from .params import PrivateSubnet2CIDR as PrivateSubnet2CIDR
from .params import VpcCIDR as VpcCIDR

__all__: list[str] = ['Base64', 'CfnEndpoint', 'CfnEndpointOutput', 'EndpointSG', 'EndpointSGAssociationParameter', 'EndpointSGEgress', 'EnvironmentName', 'GetAZs', 'Join', 'LinuxAMI', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PrivateInstance', 'PrivateInstanceAssociationParameter', 'PrivateRouteTable1', 'PrivateRouteTable1AssociationParameter', 'PrivateRouteTable2', 'PrivateRouteTable2AssociationParameter', 'PrivateSG', 'PrivateSGAssociationParameter', 'PrivateSGEgress', 'PrivateSubnet1', 'PrivateSubnet1AssociationParameter', 'PrivateSubnet1CIDR', 'PrivateSubnet1RouteTableAssociation', 'PrivateSubnet2', 'PrivateSubnet2AssociationParameter', 'PrivateSubnet2CIDR', 'PrivateSubnet2RouteTableAssociation', 'PrivateSubnetsOutput', 'PrivateWaitCondition', 'PrivateWaitHandle', 'S3Endpoint', 'S3EndpointAllowStatement0', 'S3EndpointOutput', 'S3EndpointPolicyDocument', 'STRING', 'Select', 'Sub', 'Template', 'VPC', 'VPCAssociationParameter', 'VPCOutput', 'VpcCIDR', 'cloudformation', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
