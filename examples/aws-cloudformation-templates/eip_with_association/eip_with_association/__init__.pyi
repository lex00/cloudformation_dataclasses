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
from cloudformation_dataclasses.intrinsics import Base64, Join, Select
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .compute import EC2Instance as EC2Instance
from .compute import IPAssoc as IPAssoc
from .network import IPAddress as IPAddress
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .outputs import InstanceIPAddressOutput as InstanceIPAddressOutput
from .outputs import InstanceIdOutput as InstanceIdOutput
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAmiId as LatestAmiId
from .params import SSHLocation as SSHLocation
from .params import Subnets as Subnets

__all__: list[str] = ['Base64', 'EC2Instance', 'IPAddress', 'IPAssoc', 'InstanceIPAddressOutput', 'InstanceIdOutput', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceType', 'Join', 'KeyName', 'LatestAmiId', 'Output', 'Parameter', 'ParameterType', 'SSHLocation', 'STRING', 'Select', 'Subnets', 'Template', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
