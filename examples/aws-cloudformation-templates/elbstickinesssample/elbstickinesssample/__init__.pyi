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
from cloudformation_dataclasses.aws import ec2, elasticloadbalancing
from cloudformation_dataclasses.intrinsics import (
    Base64,
    GetAZs,
    Join,
    Sub,
)

from .main import EC2Instance1 as EC2Instance1
from .main import EC2Instance2 as EC2Instance2
from .main import ElasticLoadBalancer as ElasticLoadBalancer
from .main import ElasticLoadBalancerHealthCheck as ElasticLoadBalancerHealthCheck
from .main import ElasticLoadBalancerLBCookieStickinessPolicy as ElasticLoadBalancerLBCookieStickinessPolicy
from .main import ElasticLoadBalancerListeners as ElasticLoadBalancerListeners
from .main import InstanceSecurityGroup as InstanceSecurityGroup
from .main import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .main import InstanceSecurityGroupEgress1 as InstanceSecurityGroupEgress1
from .outputs import URLOutput as URLOutput
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAmiId as LatestAmiId
from .params import Region2ExamplesMapping as Region2ExamplesMapping
from .params import SSHLocation as SSHLocation
from .params import SubnetId as SubnetId

__all__: list[str] = ['Base64', 'EC2Instance1', 'EC2Instance2', 'ElasticLoadBalancer', 'ElasticLoadBalancerHealthCheck', 'ElasticLoadBalancerLBCookieStickinessPolicy', 'ElasticLoadBalancerListeners', 'GetAZs', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceSecurityGroupEgress1', 'InstanceType', 'Join', 'KeyName', 'LatestAmiId', 'Mapping', 'Output', 'Parameter', 'ParameterType', 'Region2ExamplesMapping', 'SSHLocation', 'STRING', 'Sub', 'SubnetId', 'Template', 'URLOutput', 'cloudformation_dataclass', 'ec2', 'elasticloadbalancing', 'get_att', 'ref', 'setup_resources']
