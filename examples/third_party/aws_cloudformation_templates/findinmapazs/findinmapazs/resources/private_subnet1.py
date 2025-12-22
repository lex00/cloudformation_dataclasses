"""PrivateSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, FindInMap("RegionMap", AWS_REGION, 'AZs'))
    cidr_block = ref(PrivateSubnet1CIDR)
    map_public_ip_on_launch = False
