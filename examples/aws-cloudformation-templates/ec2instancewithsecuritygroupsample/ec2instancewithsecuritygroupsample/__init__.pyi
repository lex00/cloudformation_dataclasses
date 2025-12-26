"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
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
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import Select

from .compute import EC2Instance as EC2Instance
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .outputs import AZOutput as AZOutput
from .outputs import InstanceIdOutput as InstanceIdOutput
from .outputs import PublicDNSOutput as PublicDNSOutput
from .outputs import PublicIPOutput as PublicIPOutput
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAmiId as LatestAmiId
from .params import SSHLocation as SSHLocation
from .params import Subnets as Subnets

__all__: list[str] = ['AZOutput', 'EC2Instance', 'InstanceIdOutput', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceType', 'KeyName', 'LatestAmiId', 'Output', 'Parameter', 'ParameterType', 'PublicDNSOutput', 'PublicIPOutput', 'SSHLocation', 'STRING', 'Select', 'Subnets', 'Template', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
