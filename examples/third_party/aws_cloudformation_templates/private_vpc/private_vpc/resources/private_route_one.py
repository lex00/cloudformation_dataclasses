from __future__ import annotations

"""PrivateRouteOne - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteOne:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id: Ref[PrivateRouteTableOne] = ref()
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id: Ref[NatGatewayOne] = ref()
