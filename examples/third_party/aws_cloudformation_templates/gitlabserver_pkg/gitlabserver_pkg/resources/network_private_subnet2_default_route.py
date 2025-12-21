from __future__ import annotations

"""NetworkPrivateSubnet2DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id: Ref[NetworkPublicSubnet2NATGateway] = ref()
    route_table_id: Ref[NetworkPrivateSubnet2RouteTable] = ref()
