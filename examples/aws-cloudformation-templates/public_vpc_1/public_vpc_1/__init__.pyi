"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
    NUMBER,
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
from cloudformation_dataclasses.aws import (
    autoscaling,
    ec2,
    ecs,
    elasticloadbalancingv2,
    iam,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    AWS_STACK_NAME,
    Base64,
    FindInMap,
    GetAZs,
    Join,
    Select,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import ContainerInstances as ContainerInstances
from .compute import ContainerInstancesIamInstanceProfile as ContainerInstancesIamInstanceProfile
from .compute import ContainerInstancesLaunchTemplateData as ContainerInstancesLaunchTemplateData
from .compute import ECSAutoScalingGroup as ECSAutoScalingGroup
from .compute import ECSAutoScalingGroupLaunchTemplateSpecification as ECSAutoScalingGroupLaunchTemplateSpecification
from .compute import ECSCluster as ECSCluster
from .compute import EcsSecurityGroupIngressFromPublicALB as EcsSecurityGroupIngressFromPublicALB
from .compute import EcsSecurityGroupIngressFromSelf as EcsSecurityGroupIngressFromSelf
from .network import DummyTargetGroupPublic as DummyTargetGroupPublic
from .network import EcsHostSecurityGroup as EcsHostSecurityGroup
from .network import GatewayAttachement as GatewayAttachement
from .network import InternetGateway as InternetGateway
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
from .outputs import EcsHostSecurityGroupOutput as EcsHostSecurityGroupOutput
from .outputs import ExternalUrlOutput as ExternalUrlOutput
from .outputs import PublicListenerOutput as PublicListenerOutput
from .outputs import PublicSubnetOneOutput as PublicSubnetOneOutput
from .outputs import PublicSubnetTwoOutput as PublicSubnetTwoOutput
from .outputs import VPCIdOutput as VPCIdOutput
from .params import DesiredCapacity as DesiredCapacity
from .params import ECSAMI as ECSAMI
from .params import InstanceType as InstanceType
from .params import MaxSize as MaxSize
from .params import SubnetConfigMapping as SubnetConfigMapping
from .security import AutoscalingRole as AutoscalingRole
from .security import AutoscalingRoleAllowStatement0 as AutoscalingRoleAllowStatement0
from .security import AutoscalingRoleAllowStatement0_1 as AutoscalingRoleAllowStatement0_1
from .security import AutoscalingRoleAssumeRolePolicyDocument as AutoscalingRoleAssumeRolePolicyDocument
from .security import AutoscalingRolePolicies0PolicyDocument as AutoscalingRolePolicies0PolicyDocument
from .security import AutoscalingRolePolicy as AutoscalingRolePolicy
from .security import EC2InstanceProfile as EC2InstanceProfile
from .security import EC2Role as EC2Role
from .security import EC2RoleAllowStatement0 as EC2RoleAllowStatement0
from .security import EC2RoleAllowStatement0_1 as EC2RoleAllowStatement0_1
from .security import EC2RoleAssumeRolePolicyDocument as EC2RoleAssumeRolePolicyDocument
from .security import EC2RolePolicies0PolicyDocument as EC2RolePolicies0PolicyDocument
from .security import EC2RolePolicy as EC2RolePolicy
from .security import ECSRole as ECSRole
from .security import ECSRoleAllowStatement0 as ECSRoleAllowStatement0
from .security import ECSRoleAllowStatement0_1 as ECSRoleAllowStatement0_1
from .security import ECSRoleAssumeRolePolicyDocument as ECSRoleAssumeRolePolicyDocument
from .security import ECSRolePolicies0PolicyDocument as ECSRolePolicies0PolicyDocument
from .security import ECSRolePolicy as ECSRolePolicy

__all__: list[str] = ['AWS_REGION', 'AWS_STACK_NAME', 'AutoscalingRole', 'AutoscalingRoleAllowStatement0', 'AutoscalingRoleAllowStatement0_1', 'AutoscalingRoleAssumeRolePolicyDocument', 'AutoscalingRolePolicies0PolicyDocument', 'AutoscalingRolePolicy', 'Base64', 'ClusterNameOutput', 'ContainerInstances', 'ContainerInstancesIamInstanceProfile', 'ContainerInstancesLaunchTemplateData', 'DesiredCapacity', 'DummyTargetGroupPublic', 'EC2InstanceProfile', 'EC2Role', 'EC2RoleAllowStatement0', 'EC2RoleAllowStatement0_1', 'EC2RoleAssumeRolePolicyDocument', 'EC2RolePolicies0PolicyDocument', 'EC2RolePolicy', 'ECSAMI', 'ECSAutoScalingGroup', 'ECSAutoScalingGroupLaunchTemplateSpecification', 'ECSCluster', 'ECSRole', 'ECSRoleAllowStatement0', 'ECSRoleAllowStatement0_1', 'ECSRoleAssumeRolePolicyDocument', 'ECSRoleOutput', 'ECSRolePolicies0PolicyDocument', 'ECSRolePolicy', 'EcsHostSecurityGroup', 'EcsHostSecurityGroupOutput', 'EcsSecurityGroupIngressFromPublicALB', 'EcsSecurityGroupIngressFromSelf', 'ExternalUrlOutput', 'FindInMap', 'GatewayAttachement', 'GetAZs', 'InstanceType', 'InternetGateway', 'Join', 'Mapping', 'MaxSize', 'NUMBER', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PublicListenerOutput', 'PublicLoadBalancer', 'PublicLoadBalancerListener', 'PublicLoadBalancerListenerAction', 'PublicLoadBalancerLoadBalancerAttribute', 'PublicLoadBalancerSG', 'PublicLoadBalancerSGEgress', 'PublicRoute', 'PublicRouteTable', 'PublicSubnetOne', 'PublicSubnetOneOutput', 'PublicSubnetOneRouteTableAssociation', 'PublicSubnetTwo', 'PublicSubnetTwoOutput', 'PublicSubnetTwoRouteTableAssociation', 'STRING', 'Select', 'Sub', 'SubnetConfigMapping', 'Template', 'VPC', 'VPCIdOutput', 'autoscaling', 'cloudformation_dataclass', 'ec2', 'ecs', 'elasticloadbalancingv2', 'get_att', 'iam', 'ref', 'setup_resources']
