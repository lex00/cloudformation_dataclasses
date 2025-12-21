from __future__ import annotations

"""PrivateSubnet1DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet1DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id: Ref[PublicSubnet1NATGateway] = ref()
    route_table_id: Ref[PrivateSubnet1RouteTable] = ref()
