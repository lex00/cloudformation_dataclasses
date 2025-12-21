from __future__ import annotations

"""Eth0 - AWS::EC2::NetworkInterface resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Eth0PrivateIpAddressSpecification:
    resource: PrivateIpAddressSpecification
    private_ip_address = ref(PrimaryIPAddress)
    primary = 'true'


@cloudformation_dataclass
class Eth0PrivateIpAddressSpecification1:
    resource: PrivateIpAddressSpecification
    private_ip_address = ref(SecondaryIPAddress)
    primary = 'false'


@cloudformation_dataclass
class Eth0AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'Interface 0'


@cloudformation_dataclass
class Eth0AssociationParameter1:
    resource: AssociationParameter
    key = 'Interface'
    value = 'eth0'


@cloudformation_dataclass
class Eth0:
    """AWS::EC2::NetworkInterface resource."""

    resource: NetworkInterface
    description = 'eth0'
    group_set = [ref("SSHSecurityGroup")]
    private_ip_addresses = [Eth0PrivateIpAddressSpecification, Eth0PrivateIpAddressSpecification1]
    source_dest_check = 'true'
    subnet_id = ref(SubnetId)
    tags = [Eth0AssociationParameter, Eth0AssociationParameter1]
