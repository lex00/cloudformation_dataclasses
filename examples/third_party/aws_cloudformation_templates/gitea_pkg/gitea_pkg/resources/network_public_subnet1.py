from __future__ import annotations

"""NetworkPublicSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitea-server-public-subnet-1'


@cloudformation_dataclass
class NetworkPublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(0, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = '10.0.0.0/18'
    map_public_ip_on_launch = True
    vpc_id: Ref[NetworkVPC] = ref()
    tags = [NetworkPublicSubnet1AssociationParameter]
