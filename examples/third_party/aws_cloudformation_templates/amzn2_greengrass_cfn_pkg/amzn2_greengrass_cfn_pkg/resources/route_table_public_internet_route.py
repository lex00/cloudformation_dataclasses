from __future__ import annotations

"""RouteTablePublicInternetRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RouteTablePublicInternetRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(InternetGateway)
    route_table_id = ref(RouteTablePublic)
    depends_on = ["VPCGatewayAttachment"]
