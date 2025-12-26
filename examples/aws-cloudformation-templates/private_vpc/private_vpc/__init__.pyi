"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
    Output,
    PolicyDocument,
    PolicyStatement,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import (
    ec2,
    ecs,
    elasticloadbalancingv2,
    iam,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    AWS_STACK_NAME,
    FindInMap,
    GetAZs,
    Join,
    Select,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import ECSCluster as ECSCluster
from .compute import EcsSecurityGroupIngressFromPrivateALB as EcsSecurityGroupIngressFromPrivateALB
from .compute import EcsSecurityGroupIngressFromPublicALB as EcsSecurityGroupIngressFromPublicALB
from .compute import EcsSecurityGroupIngressFromSelf as EcsSecurityGroupIngressFromSelf
from .compute import PrivateLoadBalancerIngressFromECS as PrivateLoadBalancerIngressFromECS
from .network import DummyTargetGroupPrivate as DummyTargetGroupPrivate
from .network import DummyTargetGroupPublic as DummyTargetGroupPublic
from .network import DynamoDBEndpoint as DynamoDBEndpoint
from .network import DynamoDBEndpointAllowStatement0 as DynamoDBEndpointAllowStatement0
from .network import DynamoDBEndpointPolicyDocument as DynamoDBEndpointPolicyDocument
from .network import FargateContainerSecurityGroup as FargateContainerSecurityGroup
from .network import GatewayAttachement as GatewayAttachement
from .network import InternetGateway as InternetGateway
from .network import NatGatewayOne as NatGatewayOne
from .network import NatGatewayOneAttachment as NatGatewayOneAttachment
from .network import NatGatewayTwo as NatGatewayTwo
from .network import NatGatewayTwoAttachment as NatGatewayTwoAttachment
from .network import PrivateLoadBalancer as PrivateLoadBalancer
from .network import PrivateLoadBalancerListener as PrivateLoadBalancerListener
from .network import PrivateLoadBalancerListenerAction as PrivateLoadBalancerListenerAction
from .network import PrivateLoadBalancerLoadBalancerAttribute as PrivateLoadBalancerLoadBalancerAttribute
from .network import PrivateLoadBalancerSG as PrivateLoadBalancerSG
from .network import PrivateRouteOne as PrivateRouteOne
from .network import PrivateRouteTableOne as PrivateRouteTableOne
from .network import PrivateRouteTableOneAssociation as PrivateRouteTableOneAssociation
from .network import PrivateRouteTableTwo as PrivateRouteTableTwo
from .network import PrivateRouteTableTwoAssociation as PrivateRouteTableTwoAssociation
from .network import PrivateRouteTwo as PrivateRouteTwo
from .network import PrivateSubnetOne as PrivateSubnetOne
from .network import PrivateSubnetTwo as PrivateSubnetTwo
from .network import PublicLoadBalancer as PublicLoadBalancer
from .network import PublicLoadBalancerListener as PublicLoadBalancerListener
from .network import PublicLoadBalancerListenerAction as PublicLoadBalancerListenerAction
from .network import PublicLoadBalancerLoadBalancerAttribute as PublicLoadBalancerLoadBalancerAttribute
from .network import PublicLoadBalancerSG as PublicLoadBalancerSG
from .network import PublicLoadBalancerSGEgress as PublicLoadBalancerSGEgress
from .network import PublicRoute as PublicRoute
from .network import PublicRouteTable as PublicRouteTable
from .network import PublicSubnetOne as PublicSubnetOne
from .network import PublicSubnetOneRouteTableAssociation as PublicSubnetOneRouteTableAssociation
from .network import PublicSubnetTwo as PublicSubnetTwo
from .network import PublicSubnetTwoRouteTableAssociation as PublicSubnetTwoRouteTableAssociation
from .network import VPC as VPC
from .outputs import ClusterNameOutput as ClusterNameOutput
from .outputs import ECSRoleOutput as ECSRoleOutput
from .outputs import ECSTaskExecutionRoleOutput as ECSTaskExecutionRoleOutput
from .outputs import ExternalUrlOutput as ExternalUrlOutput
from .outputs import FargateContainerSecurityGroupOutput as FargateContainerSecurityGroupOutput
from .outputs import InternalUrlOutput as InternalUrlOutput
from .outputs import PrivateListenerOutput as PrivateListenerOutput
from .outputs import PrivateSubnetOneOutput as PrivateSubnetOneOutput
from .outputs import PrivateSubnetTwoOutput as PrivateSubnetTwoOutput
from .outputs import PublicListenerOutput as PublicListenerOutput
from .outputs import PublicSubnetOneOutput as PublicSubnetOneOutput
from .outputs import PublicSubnetTwoOutput as PublicSubnetTwoOutput
from .outputs import VPCIdOutput as VPCIdOutput
from .params import SubnetConfigMapping as SubnetConfigMapping
from .security import ECSRole as ECSRole
from .security import ECSRoleAllowStatement0 as ECSRoleAllowStatement0
from .security import ECSRoleAllowStatement0_1 as ECSRoleAllowStatement0_1
from .security import ECSRoleAssumeRolePolicyDocument as ECSRoleAssumeRolePolicyDocument
from .security import ECSRolePolicies0PolicyDocument as ECSRolePolicies0PolicyDocument
from .security import ECSRolePolicy as ECSRolePolicy
from .security import ECSTaskExecutionRole as ECSTaskExecutionRole
from .security import ECSTaskExecutionRoleAllowStatement0 as ECSTaskExecutionRoleAllowStatement0
from .security import ECSTaskExecutionRoleAllowStatement0_1 as ECSTaskExecutionRoleAllowStatement0_1
from .security import ECSTaskExecutionRoleAssumeRolePolicyDocument as ECSTaskExecutionRoleAssumeRolePolicyDocument
from .security import ECSTaskExecutionRolePolicies0PolicyDocument as ECSTaskExecutionRolePolicies0PolicyDocument
from .security import ECSTaskExecutionRolePolicy as ECSTaskExecutionRolePolicy

__all__: list[str] = ['AWS_REGION', 'AWS_STACK_NAME', 'ClusterNameOutput', 'DummyTargetGroupPrivate', 'DummyTargetGroupPublic', 'DynamoDBEndpoint', 'DynamoDBEndpointAllowStatement0', 'DynamoDBEndpointPolicyDocument', 'ECSCluster', 'ECSRole', 'ECSRoleAllowStatement0', 'ECSRoleAllowStatement0_1', 'ECSRoleAssumeRolePolicyDocument', 'ECSRoleOutput', 'ECSRolePolicies0PolicyDocument', 'ECSRolePolicy', 'ECSTaskExecutionRole', 'ECSTaskExecutionRoleAllowStatement0', 'ECSTaskExecutionRoleAllowStatement0_1', 'ECSTaskExecutionRoleAssumeRolePolicyDocument', 'ECSTaskExecutionRoleOutput', 'ECSTaskExecutionRolePolicies0PolicyDocument', 'ECSTaskExecutionRolePolicy', 'EcsSecurityGroupIngressFromPrivateALB', 'EcsSecurityGroupIngressFromPublicALB', 'EcsSecurityGroupIngressFromSelf', 'ExternalUrlOutput', 'FargateContainerSecurityGroup', 'FargateContainerSecurityGroupOutput', 'FindInMap', 'GatewayAttachement', 'GetAZs', 'InternalUrlOutput', 'InternetGateway', 'Join', 'Mapping', 'NatGatewayOne', 'NatGatewayOneAttachment', 'NatGatewayTwo', 'NatGatewayTwoAttachment', 'Output', 'PolicyDocument', 'PolicyStatement', 'PrivateListenerOutput', 'PrivateLoadBalancer', 'PrivateLoadBalancerIngressFromECS', 'PrivateLoadBalancerListener', 'PrivateLoadBalancerListenerAction', 'PrivateLoadBalancerLoadBalancerAttribute', 'PrivateLoadBalancerSG', 'PrivateRouteOne', 'PrivateRouteTableOne', 'PrivateRouteTableOneAssociation', 'PrivateRouteTableTwo', 'PrivateRouteTableTwoAssociation', 'PrivateRouteTwo', 'PrivateSubnetOne', 'PrivateSubnetOneOutput', 'PrivateSubnetTwo', 'PrivateSubnetTwoOutput', 'PublicListenerOutput', 'PublicLoadBalancer', 'PublicLoadBalancerListener', 'PublicLoadBalancerListenerAction', 'PublicLoadBalancerLoadBalancerAttribute', 'PublicLoadBalancerSG', 'PublicLoadBalancerSGEgress', 'PublicRoute', 'PublicRouteTable', 'PublicSubnetOne', 'PublicSubnetOneOutput', 'PublicSubnetOneRouteTableAssociation', 'PublicSubnetTwo', 'PublicSubnetTwoOutput', 'PublicSubnetTwoRouteTableAssociation', 'Select', 'SubnetConfigMapping', 'Template', 'VPC', 'VPCIdOutput', 'cloudformation_dataclass', 'ec2', 'ecs', 'elasticloadbalancingv2', 'get_att', 'iam', 'ref', 'setup_resources']
