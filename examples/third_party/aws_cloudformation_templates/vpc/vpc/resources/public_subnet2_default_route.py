from __future__ import annotations

"""PublicSubnet2DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    route_table_id = ref(PublicSubnet2RouteTable)
    depends_on = ["VPCGW"]
