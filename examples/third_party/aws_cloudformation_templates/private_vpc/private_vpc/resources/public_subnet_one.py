from __future__ import annotations

"""PublicSubnetOne - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetOne:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(0, GetAZs({'Ref': 'AWS::Region'}))
    vpc_id: Ref[VPC] = ref()
    cidr_block = FindInMap("SubnetConfig", 'PublicOne', 'CIDR')
    map_public_ip_on_launch = True
