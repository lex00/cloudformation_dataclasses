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
from .compute import EC2InstanceBlockDeviceMapping as EC2InstanceBlockDeviceMapping
from .network import EC2SecurityGroup as EC2SecurityGroup
from .network import EC2SecurityGroupEgress as EC2SecurityGroupEgress
from .outputs import InstanceOutput as InstanceOutput
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAmiId as LatestAmiId
from .params import SSHLocation as SSHLocation
from .params import Subnets as Subnets

__all__: list[str] = ['EC2Instance', 'EC2InstanceBlockDeviceMapping', 'EC2SecurityGroup', 'EC2SecurityGroupEgress', 'InstanceOutput', 'InstanceType', 'KeyName', 'LatestAmiId', 'Output', 'Parameter', 'ParameterType', 'SSHLocation', 'STRING', 'Select', 'Subnets', 'Template', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
