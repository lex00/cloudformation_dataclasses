from __future__ import annotations

"""PublicSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1AssociationParameter:
    resource: AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicSubnet1AssociationParameter1:
    resource: AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicSubnet1AssociationParameter2:
    resource: AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-',
    Select(1, GetAZs()),
])


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(1, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Public1', 'CIDR')
    map_public_ip_on_launch = 'true'
    tags = [PublicSubnet1AssociationParameter, PublicSubnet1AssociationParameter1, PublicSubnet1AssociationParameter2]
