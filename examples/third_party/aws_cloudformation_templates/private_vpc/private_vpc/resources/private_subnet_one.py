from __future__ import annotations

"""PrivateSubnetOne - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnetOne:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(0, GetAZs({'Ref': 'AWS::Region'}))
    vpc_id: Ref[VPC] = ref()
    cidr_block = FindInMap("SubnetConfig", 'PrivateOne', 'CIDR')
