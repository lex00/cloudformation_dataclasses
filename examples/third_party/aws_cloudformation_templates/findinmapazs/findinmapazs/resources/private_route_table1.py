"""PrivateRouteTable1 - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTable1:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id = ref(VPC)
