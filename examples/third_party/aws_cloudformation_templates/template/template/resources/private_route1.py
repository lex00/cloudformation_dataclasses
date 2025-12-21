from __future__ import annotations

"""PrivateRoute1 - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRoute1:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id: Ref[PrivateRouteTable1] = ref()
    nat_gateway_id: Ref[NATGateway1] = ref()
    destination_cidr_block = '0.0.0.0/0'
