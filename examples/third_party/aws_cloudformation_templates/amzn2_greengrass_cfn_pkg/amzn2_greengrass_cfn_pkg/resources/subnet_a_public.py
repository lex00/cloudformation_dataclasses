from __future__ import annotations

"""SubnetAPublic - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SubnetAPublic:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = get_att(InstanceAZ, "AvailabilityZone")
    cidr_block = '172.31.0.0/24'
    map_public_ip_on_launch = True
    vpc_id = ref(VPC)
