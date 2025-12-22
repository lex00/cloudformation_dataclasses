from __future__ import annotations

"""PublicRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id: Ref[PublicRouteTable] = ref()
    destination_cidr_block = '0.0.0.0/0'
    gateway_id: Ref[InternetGateway] = ref()
    depends_on = ["GatewayToInternet"]
