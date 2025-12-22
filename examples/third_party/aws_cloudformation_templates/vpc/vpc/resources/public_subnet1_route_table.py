"""PublicSubnet1RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id = ref(VPC)
