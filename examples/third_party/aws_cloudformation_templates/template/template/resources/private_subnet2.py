from __future__ import annotations

"""PrivateSubnet2 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet2AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-subnet2')


@cloudformation_dataclass
class PrivateSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(1, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = ref(PrivateCidrBlock2)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet2AssociationParameter]
