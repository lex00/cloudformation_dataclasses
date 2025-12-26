"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
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
from cloudformation_dataclasses.aws import (
    autoscaling,
    cloudwatch,
    ec2,
    efs,
    elasticloadbalancing,
    iam,
)
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    AWS_STACK_NAME,
    Base64,
    FindInMap,
    Join,
    Select,
    Sub,
)

from .compute import AutoScalingGroup as AutoScalingGroup
from .compute import LaunchConfig as LaunchConfig
from .compute import ScaleDownPolicy as ScaleDownPolicy
from .compute import ScaleUpPolicy as ScaleUpPolicy
from .monitoring import CPUAlarmHigh as CPUAlarmHigh
from .monitoring import CPUAlarmHighDimension as CPUAlarmHighDimension
from .monitoring import CPUAlarmLow as CPUAlarmLow
from .monitoring import CPUAlarmLowDimension as CPUAlarmLowDimension
from .network import EFSSecurityGroup as EFSSecurityGroup
from .network import EFSSecurityGroupIngress as EFSSecurityGroupIngress
from .network import ELBSecurityGroup as ELBSecurityGroup
from .network import ELBSecurityGroupEgress as ELBSecurityGroupEgress
from .network import ELBSecurityGroupEgress1 as ELBSecurityGroupEgress1
from .network import ElasticLoadBalancer as ElasticLoadBalancer
from .network import ElasticLoadBalancerHealthCheck as ElasticLoadBalancerHealthCheck
from .network import ElasticLoadBalancerListeners as ElasticLoadBalancerListeners
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .network import InstanceSecurityGroupIngress as InstanceSecurityGroupIngress
from .outputs import AutoScalingGroupOutput as AutoScalingGroupOutput
from .outputs import StackNameOutput as StackNameOutput
from .outputs import URLOutput as URLOutput
from .params import EC2RegionMapMapping as EC2RegionMapMapping
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import Subnets as Subnets
from .params import VPC as VPC
from .security import IAMAssumeInstanceRole as IAMAssumeInstanceRole
from .security import IAMAssumeInstanceRoleAllowStatement0 as IAMAssumeInstanceRoleAllowStatement0
from .security import IAMAssumeInstanceRoleAllowStatement0_1 as IAMAssumeInstanceRoleAllowStatement0_1
from .security import IAMAssumeInstanceRoleAllowStatement1 as IAMAssumeInstanceRoleAllowStatement1
from .security import IAMAssumeInstanceRoleAllowStatement2 as IAMAssumeInstanceRoleAllowStatement2
from .security import IAMAssumeInstanceRoleAssumeRolePolicyDocument as IAMAssumeInstanceRoleAssumeRolePolicyDocument
from .security import IAMAssumeInstanceRolePolicies0PolicyDocument as IAMAssumeInstanceRolePolicies0PolicyDocument
from .security import IAMAssumeInstanceRolePolicy as IAMAssumeInstanceRolePolicy
from .security import InstanceProfile as InstanceProfile
from .storage import EFSFileSystem as EFSFileSystem
from .storage import EFSMountTarget1 as EFSMountTarget1
from .storage import EFSMountTarget2 as EFSMountTarget2
from .storage import EFSMountTarget3 as EFSMountTarget3
from .storage import EFSMountTarget4 as EFSMountTarget4

__all__: list[str] = ['AWS_REGION', 'AWS_STACK_NAME', 'AutoScalingGroup', 'AutoScalingGroupOutput', 'Base64', 'CPUAlarmHigh', 'CPUAlarmHighDimension', 'CPUAlarmLow', 'CPUAlarmLowDimension', 'EC2RegionMapMapping', 'EFSFileSystem', 'EFSMountTarget1', 'EFSMountTarget2', 'EFSMountTarget3', 'EFSMountTarget4', 'EFSSecurityGroup', 'EFSSecurityGroupIngress', 'ELBSecurityGroup', 'ELBSecurityGroupEgress', 'ELBSecurityGroupEgress1', 'ElasticLoadBalancer', 'ElasticLoadBalancerHealthCheck', 'ElasticLoadBalancerListeners', 'FindInMap', 'IAMAssumeInstanceRole', 'IAMAssumeInstanceRoleAllowStatement0', 'IAMAssumeInstanceRoleAllowStatement0_1', 'IAMAssumeInstanceRoleAllowStatement1', 'IAMAssumeInstanceRoleAllowStatement2', 'IAMAssumeInstanceRoleAssumeRolePolicyDocument', 'IAMAssumeInstanceRolePolicies0PolicyDocument', 'IAMAssumeInstanceRolePolicy', 'InstanceProfile', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceSecurityGroupIngress', 'InstanceType', 'Join', 'KeyName', 'LaunchConfig', 'Mapping', 'Output', 'Parameter', 'ParameterType', 'PolicyDocument', 'PolicyStatement', 'STRING', 'ScaleDownPolicy', 'ScaleUpPolicy', 'Select', 'StackNameOutput', 'Sub', 'Subnets', 'Template', 'URLOutput', 'VPC', 'autoscaling', 'cloudformation_dataclass', 'cloudwatch', 'ec2', 'efs', 'elasticloadbalancing', 'get_att', 'iam', 'ref', 'setup_resources']
