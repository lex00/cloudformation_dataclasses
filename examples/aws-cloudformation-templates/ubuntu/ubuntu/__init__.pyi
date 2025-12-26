"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
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
from cloudformation_dataclasses.intrinsics import Base64, Sub

from .compute import EC2Instance as EC2Instance
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .params import IAMRole as IAMRole
from .params import InstanceAMI as InstanceAMI
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import SSHLocation as SSHLocation
from .params import SSMKey as SSMKey
from .params import SubnetId as SubnetId

__all__: list[str] = ['Base64', 'EC2Instance', 'IAMRole', 'InstanceAMI', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceType', 'KeyName', 'Parameter', 'ParameterType', 'SSHLocation', 'SSMKey', 'STRING', 'Sub', 'SubnetId', 'Template', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
