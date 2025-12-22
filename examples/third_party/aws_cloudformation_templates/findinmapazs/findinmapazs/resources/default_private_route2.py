from __future__ import annotations

"""DefaultPrivateRoute2 - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DefaultPrivateRoute2:
    """AWS::EC2::Route resource."""

    resource: Route
    route_table_id = ref(PrivateRouteTable2)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NatGateway2)
