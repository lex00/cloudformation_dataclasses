from __future__ import annotations

"""NetworkPublicSubnet2DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id: Ref[NetworkInternetGateway] = ref()
    route_table_id: Ref[NetworkPublicSubnet2RouteTable] = ref()
    depends_on = ["NetworkVPCGW"]
