"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
    Output,
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import autoscaling, ec2, elasticloadbalancing
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    Base64,
    FindInMap,
    GetAZs,
    Join,
    Sub,
)
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import LaunchTemplate as LaunchTemplate
from .compute import LaunchTemplateSpotFleetLaunchSpecification as LaunchTemplateSpotFleetLaunchSpecification
from .compute import ScheduledActionDown as ScheduledActionDown
from .compute import ScheduledActionUp as ScheduledActionUp
from .compute import WebServerGroup as WebServerGroup
from .compute import WebServerGroupLaunchTemplateSpecification as WebServerGroupLaunchTemplateSpecification
from .network import ElasticLoadBalancer as ElasticLoadBalancer
from .network import ElasticLoadBalancerHealthCheck as ElasticLoadBalancerHealthCheck
from .network import ElasticLoadBalancerListeners as ElasticLoadBalancerListeners
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .network import InstanceSecurityGroupEgress1 as InstanceSecurityGroupEgress1
from .outputs import URLOutput as URLOutput
from .params import AWSInstanceType2ArchMapping as AWSInstanceType2ArchMapping
from .params import AWSRegionArch2AMIMapping as AWSRegionArch2AMIMapping
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import Region2ExamplesMapping as Region2ExamplesMapping
from .params import SSHLocation as SSHLocation

__all__: list[str] = ['AWSInstanceType2ArchMapping', 'AWSRegionArch2AMIMapping', 'AWS_REGION', 'Base64', 'ElasticLoadBalancer', 'ElasticLoadBalancerHealthCheck', 'ElasticLoadBalancerListeners', 'FindInMap', 'GetAZs', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceSecurityGroupEgress1', 'InstanceType', 'Join', 'KeyName', 'LaunchTemplate', 'LaunchTemplateSpotFleetLaunchSpecification', 'Mapping', 'Output', 'Parameter', 'ParameterType', 'Region2ExamplesMapping', 'SSHLocation', 'STRING', 'ScheduledActionDown', 'ScheduledActionUp', 'Sub', 'Template', 'URLOutput', 'WebServerGroup', 'WebServerGroupLaunchTemplateSpecification', 'autoscaling', 'cloudformation_dataclass', 'ec2', 'elasticloadbalancing', 'get_att', 'ref', 'setup_resources']
