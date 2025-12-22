from __future__ import annotations

"""PrivateSubnetTwo - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnetTwo:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(1, GetAZs({'Ref': 'AWS::Region'}))
    vpc_id: Ref[VPC] = ref()
    cidr_block = FindInMap("SubnetConfig", 'PrivateTwo', 'CIDR')
