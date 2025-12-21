from __future__ import annotations

"""NetworkPrivateSubnet1Subnet - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet1SubnetAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-1'


@cloudformation_dataclass
class NetworkPrivateSubnet1Subnet:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(0, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id: Ref[NetworkVPC] = ref()
    tags = [NetworkPrivateSubnet1SubnetAssociationParameter]
