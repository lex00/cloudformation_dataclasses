from __future__ import annotations

"""NetworkPublicSubnet2 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-2'


@cloudformation_dataclass
class NetworkPublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(1, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id: Ref[NetworkVPC] = ref()
    tags = [NetworkPublicSubnet2AssociationParameter]
