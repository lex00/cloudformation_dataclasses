from __future__ import annotations

"""PrivateSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet1')


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(0, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = ref(PrivateCidrBlock1)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet1AssociationParameter]
