from __future__ import annotations

"""RouteInternetGateway - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RouteInternetGateway:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id: Ref[PublicRouteTable] = ref()
    gateway_id: Ref[InternetGateway] = ref()
    destination_cidr_block = '0.0.0.0/0'
