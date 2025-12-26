"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
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
from cloudformation_dataclasses.aws import cloudfront, ec2, iam
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    Base64,
    FindInMap,
    GetAZs,
    Select,
    Sub,
)

from .main import CloudFrontCachePolicy as CloudFrontCachePolicy
from .main import CloudFrontCachePolicyCachePolicyConfig as CloudFrontCachePolicyCachePolicyConfig
from .main import CloudFrontCachePolicyCookiesConfig as CloudFrontCachePolicyCookiesConfig
from .main import CloudFrontCachePolicyHeadersConfig as CloudFrontCachePolicyHeadersConfig
from .main import CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin as CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin
from .main import CloudFrontCachePolicyQueryStringsConfig as CloudFrontCachePolicyQueryStringsConfig
from .main import CloudFrontDistribution as CloudFrontDistribution
from .main import CloudFrontDistributionCacheBehavior as CloudFrontDistributionCacheBehavior
from .main import CloudFrontDistributionCustomOriginConfig as CloudFrontDistributionCustomOriginConfig
from .main import CloudFrontDistributionDefaultCacheBehavior as CloudFrontDistributionDefaultCacheBehavior
from .main import CloudFrontDistributionDistributionConfig as CloudFrontDistributionDistributionConfig
from .main import CloudFrontDistributionOrigin as CloudFrontDistributionOrigin
from .main import InstanceSecurityGroup as InstanceSecurityGroup
from .main import InstanceSecurityGroupAssociationParameter as InstanceSecurityGroupAssociationParameter
from .main import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .main import InstanceSecurityGroupIngress as InstanceSecurityGroupIngress
from .main import NetworkInternetGateway as NetworkInternetGateway
from .main import NetworkInternetGatewayAssociationParameter as NetworkInternetGatewayAssociationParameter
from .main import NetworkPrivateSubnet1DefaultRoute as NetworkPrivateSubnet1DefaultRoute
from .main import NetworkPrivateSubnet1RouteTable as NetworkPrivateSubnet1RouteTable
from .main import NetworkPrivateSubnet1RouteTableAssociation as NetworkPrivateSubnet1RouteTableAssociation
from .main import NetworkPrivateSubnet1RouteTableAssociationParameter as NetworkPrivateSubnet1RouteTableAssociationParameter
from .main import NetworkPrivateSubnet1Subnet as NetworkPrivateSubnet1Subnet
from .main import NetworkPrivateSubnet1SubnetAssociationParameter as NetworkPrivateSubnet1SubnetAssociationParameter
from .main import NetworkPrivateSubnet2DefaultRoute as NetworkPrivateSubnet2DefaultRoute
from .main import NetworkPrivateSubnet2RouteTable as NetworkPrivateSubnet2RouteTable
from .main import NetworkPrivateSubnet2RouteTableAssociation as NetworkPrivateSubnet2RouteTableAssociation
from .main import NetworkPrivateSubnet2RouteTableAssociationParameter as NetworkPrivateSubnet2RouteTableAssociationParameter
from .main import NetworkPrivateSubnet2Subnet as NetworkPrivateSubnet2Subnet
from .main import NetworkPrivateSubnet2SubnetAssociationParameter as NetworkPrivateSubnet2SubnetAssociationParameter
from .main import NetworkPublicSubnet1 as NetworkPublicSubnet1
from .main import NetworkPublicSubnet1AssociationParameter as NetworkPublicSubnet1AssociationParameter
from .main import NetworkPublicSubnet1DefaultRoute as NetworkPublicSubnet1DefaultRoute
from .main import NetworkPublicSubnet1EIP as NetworkPublicSubnet1EIP
from .main import NetworkPublicSubnet1EIPAssociationParameter as NetworkPublicSubnet1EIPAssociationParameter
from .main import NetworkPublicSubnet1NATGateway as NetworkPublicSubnet1NATGateway
from .main import NetworkPublicSubnet1NATGatewayAssociationParameter as NetworkPublicSubnet1NATGatewayAssociationParameter
from .main import NetworkPublicSubnet1RouteTable as NetworkPublicSubnet1RouteTable
from .main import NetworkPublicSubnet1RouteTableAssociation as NetworkPublicSubnet1RouteTableAssociation
from .main import NetworkPublicSubnet1RouteTableAssociationParameter as NetworkPublicSubnet1RouteTableAssociationParameter
from .main import NetworkPublicSubnet2 as NetworkPublicSubnet2
from .main import NetworkPublicSubnet2AssociationParameter as NetworkPublicSubnet2AssociationParameter
from .main import NetworkPublicSubnet2DefaultRoute as NetworkPublicSubnet2DefaultRoute
from .main import NetworkPublicSubnet2EIP as NetworkPublicSubnet2EIP
from .main import NetworkPublicSubnet2EIPAssociationParameter as NetworkPublicSubnet2EIPAssociationParameter
from .main import NetworkPublicSubnet2NATGateway as NetworkPublicSubnet2NATGateway
from .main import NetworkPublicSubnet2NATGatewayAssociationParameter as NetworkPublicSubnet2NATGatewayAssociationParameter
from .main import NetworkPublicSubnet2RouteTable as NetworkPublicSubnet2RouteTable
from .main import NetworkPublicSubnet2RouteTableAssociation as NetworkPublicSubnet2RouteTableAssociation
from .main import NetworkPublicSubnet2RouteTableAssociationParameter as NetworkPublicSubnet2RouteTableAssociationParameter
from .main import NetworkVPC as NetworkVPC
from .main import NetworkVPCAssociationParameter as NetworkVPCAssociationParameter
from .main import NetworkVPCGW as NetworkVPCGW
from .main import Server as Server
from .main import ServerAssociationParameter as ServerAssociationParameter
from .main import ServerBlockDeviceMapping as ServerBlockDeviceMapping
from .main import ServerEbs as ServerEbs
from .outputs import URLOutput as URLOutput
from .params import InstanceType as InstanceType
from .params import LatestAMI as LatestAMI
from .params import PrefixesMapping as PrefixesMapping
from .params import SecretName as SecretName
from .security import InstanceProfile as InstanceProfile
from .security import InstanceRole as InstanceRole
from .security import InstanceRoleAllowStatement0 as InstanceRoleAllowStatement0
from .security import InstanceRoleAssumeRolePolicyDocument as InstanceRoleAssumeRolePolicyDocument
from .security import InstanceRolePolicy as InstanceRolePolicy
from .security import InstanceRolePolicyAllowStatement0 as InstanceRolePolicyAllowStatement0
from .security import InstanceRolePolicyPolicyDocument as InstanceRolePolicyPolicyDocument

__all__: list[str] = ['AWS_REGION', 'Base64', 'CloudFrontCachePolicy', 'CloudFrontCachePolicyCachePolicyConfig', 'CloudFrontCachePolicyCookiesConfig', 'CloudFrontCachePolicyHeadersConfig', 'CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin', 'CloudFrontCachePolicyQueryStringsConfig', 'CloudFrontDistribution', 'CloudFrontDistributionCacheBehavior', 'CloudFrontDistributionCustomOriginConfig', 'CloudFrontDistributionDefaultCacheBehavior', 'CloudFrontDistributionDistributionConfig', 'CloudFrontDistributionOrigin', 'FindInMap', 'GetAZs', 'InstanceProfile', 'InstanceRole', 'InstanceRoleAllowStatement0', 'InstanceRoleAssumeRolePolicyDocument', 'InstanceRolePolicy', 'InstanceRolePolicyAllowStatement0', 'InstanceRolePolicyPolicyDocument', 'InstanceSecurityGroup', 'InstanceSecurityGroupAssociationParameter', 'InstanceSecurityGroupEgress', 'InstanceSecurityGroupIngress', 'InstanceType', 'LatestAMI', 'Mapping', 'NetworkInternetGateway', 'NetworkInternetGatewayAssociationParameter', 'NetworkPrivateSubnet1DefaultRoute', 'NetworkPrivateSubnet1RouteTable', 'NetworkPrivateSubnet1RouteTableAssociation', 'NetworkPrivateSubnet1RouteTableAssociationParameter', 'NetworkPrivateSubnet1Subnet', 'NetworkPrivateSubnet1SubnetAssociationParameter', 'NetworkPrivateSubnet2DefaultRoute', 'NetworkPrivateSubnet2RouteTable', 'NetworkPrivateSubnet2RouteTableAssociation', 'NetworkPrivateSubnet2RouteTableAssociationParameter', 'NetworkPrivateSubnet2Subnet', 'NetworkPrivateSubnet2SubnetAssociationParameter', 'NetworkPublicSubnet1', 'NetworkPublicSubnet1AssociationParameter', 'NetworkPublicSubnet1DefaultRoute', 'NetworkPublicSubnet1EIP', 'NetworkPublicSubnet1EIPAssociationParameter', 'NetworkPublicSubnet1NATGateway', 'NetworkPublicSubnet1NATGatewayAssociationParameter', 'NetworkPublicSubnet1RouteTable', 'NetworkPublicSubnet1RouteTableAssociation', 'NetworkPublicSubnet1RouteTableAssociationParameter', 'NetworkPublicSubnet2', 'NetworkPublicSubnet2AssociationParameter', 'NetworkPublicSubnet2DefaultRoute', 'NetworkPublicSubnet2EIP', 'NetworkPublicSubnet2EIPAssociationParameter', 'NetworkPublicSubnet2NATGateway', 'NetworkPublicSubnet2NATGatewayAssociationParameter', 'NetworkPublicSubnet2RouteTable', 'NetworkPublicSubnet2RouteTableAssociation', 'NetworkPublicSubnet2RouteTableAssociationParameter', 'NetworkVPC', 'NetworkVPCAssociationParameter', 'NetworkVPCGW', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PrefixesMapping', 'STRING', 'SecretName', 'Select', 'Server', 'ServerAssociationParameter', 'ServerBlockDeviceMapping', 'ServerEbs', 'Sub', 'Template', 'URLOutput', 'cloudformation_dataclass', 'cloudfront', 'ec2', 'get_att', 'iam', 'ref', 'setup_resources']
