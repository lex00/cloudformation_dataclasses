from __future__ import annotations

"""PrivateSubnet3 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet3AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet3')


@cloudformation_dataclass
class PrivateSubnet3:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(2, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = ref(PrivateCidrBlock3)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet3AssociationParameter]
