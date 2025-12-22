from __future__ import annotations

"""PublicSubnetTwo - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetTwo:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(1, GetAZs({'Ref': 'AWS::Region'}))
    vpc_id: Ref[VPC] = ref()
    cidr_block = FindInMap("SubnetConfig", 'PublicTwo', 'CIDR')
    map_public_ip_on_launch = True
