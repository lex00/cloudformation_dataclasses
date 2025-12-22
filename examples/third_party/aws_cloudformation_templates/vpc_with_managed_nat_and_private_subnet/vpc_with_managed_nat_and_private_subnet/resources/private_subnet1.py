from __future__ import annotations

"""PrivateSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter:
    resource: AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter1:
    resource: AssociationParameter
    key = 'Network'
    value = 'Private'


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter2:
    resource: AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-private-',
    Select(1, GetAZs()),
])


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(1, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Private1', 'CIDR')
    tags = [PrivateSubnet1AssociationParameter, PrivateSubnet1AssociationParameter1, PrivateSubnet1AssociationParameter2]
