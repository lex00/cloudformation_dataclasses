from __future__ import annotations

"""PrivateRouteTwo - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTwo:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id: Ref[PrivateRouteTableTwo] = ref()
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id: Ref[NatGatewayTwo] = ref()
