from __future__ import annotations

"""PrivateSubnet2DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id: Ref[PublicSubnet2NATGateway] = ref()
    route_table_id: Ref[PrivateSubnet2RouteTable] = ref()
