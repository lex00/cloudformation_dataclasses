from __future__ import annotations

"""PrivateRoute3 - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRoute3:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id: Ref[PrivateRouteTable3] = ref()
    nat_gateway_id: Ref[NATGateway3] = ref()
    destination_cidr_block = '0.0.0.0/0'
