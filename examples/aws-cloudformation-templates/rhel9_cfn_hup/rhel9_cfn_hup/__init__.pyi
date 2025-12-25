"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import (
    AWS_REGION,
    Base64,
    FindInMap,
    Sub,
)
from .params import *  # noqa: F403, F401

from .compute import EC2Instance as EC2Instance
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .params import AWSInstanceType2ArchMapping as AWSInstanceType2ArchMapping
from .params import AWSRegionArch2AMIMapping as AWSRegionArch2AMIMapping
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import SSHLocation as SSHLocation
from .params import SubnetId as SubnetId

__all__: list[str] = ['AWSInstanceType2ArchMapping', 'AWSRegionArch2AMIMapping', 'AWS_REGION', 'Base64', 'EC2Instance', 'FindInMap', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceType', 'KeyName', 'Mapping', 'Parameter', 'ParameterType', 'SSHLocation', 'STRING', 'Sub', 'SubnetId', 'Template', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
