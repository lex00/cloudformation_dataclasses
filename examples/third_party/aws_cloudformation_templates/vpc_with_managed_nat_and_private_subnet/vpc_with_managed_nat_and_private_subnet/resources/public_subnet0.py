from __future__ import annotations

"""PublicSubnet0 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet0AssociationParameter:
    resource: AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicSubnet0AssociationParameter1:
    resource: AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicSubnet0AssociationParameter2:
    resource: AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-',
    Select(0, GetAZs()),
])


@cloudformation_dataclass
class PublicSubnet0:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(0, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Public0', 'CIDR')
    map_public_ip_on_launch = 'true'
    tags = [PublicSubnet0AssociationParameter, PublicSubnet0AssociationParameter1, PublicSubnet0AssociationParameter2]
