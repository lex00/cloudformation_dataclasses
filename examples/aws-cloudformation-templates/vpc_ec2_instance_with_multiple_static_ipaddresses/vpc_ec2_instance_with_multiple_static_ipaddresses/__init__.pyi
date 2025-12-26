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
from cloudformation_dataclasses.intrinsics import Join, Select

from .compute import EC2Instance as EC2Instance
from .compute import EC2InstanceAssociationParameter as EC2InstanceAssociationParameter
from .compute import EC2InstanceInstanceNetworkInterfaceSpecification as EC2InstanceInstanceNetworkInterfaceSpecification
from .compute import EIPAssoc1 as EIPAssoc1
from .network import EIP1 as EIP1
from .network import Eth0 as Eth0
from .network import Eth0AssociationParameter as Eth0AssociationParameter
from .network import Eth0AssociationParameter1 as Eth0AssociationParameter1
from .network import Eth0PrivateIpAddressSpecification as Eth0PrivateIpAddressSpecification
from .network import Eth0PrivateIpAddressSpecification1 as Eth0PrivateIpAddressSpecification1
from .network import SSHSecurityGroup as SSHSecurityGroup
from .network import SSHSecurityGroupEgress as SSHSecurityGroupEgress
from .outputs import EIP1Output as EIP1Output
from .outputs import InstanceIdOutput as InstanceIdOutput
from .outputs import PrimaryPrivateIPAddressOutput as PrimaryPrivateIPAddressOutput
from .outputs import SecondaryPrivateIPAddressesOutput as SecondaryPrivateIPAddressesOutput
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAMI as LatestAMI
from .params import PrimaryIPAddress as PrimaryIPAddress
from .params import SSHLocation as SSHLocation
from .params import SecondaryIPAddress as SecondaryIPAddress
from .params import SubnetId as SubnetId
from .params import VpcId as VpcId

__all__: list[str] = ['EC2Instance', 'EC2InstanceAssociationParameter', 'EC2InstanceInstanceNetworkInterfaceSpecification', 'EIP1', 'EIP1Output', 'EIPAssoc1', 'Eth0', 'Eth0AssociationParameter', 'Eth0AssociationParameter1', 'Eth0PrivateIpAddressSpecification', 'Eth0PrivateIpAddressSpecification1', 'InstanceIdOutput', 'InstanceType', 'Join', 'KeyName', 'LatestAMI', 'Output', 'Parameter', 'ParameterType', 'PrimaryIPAddress', 'PrimaryPrivateIPAddressOutput', 'SSHLocation', 'SSHSecurityGroup', 'SSHSecurityGroupEgress', 'STRING', 'SecondaryIPAddress', 'SecondaryPrivateIPAddressesOutput', 'Select', 'SubnetId', 'Template', 'VpcId', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
