from __future__ import annotations

"""PublicSubnet2DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id: Ref[InternetGateway] = ref()
    route_table_id: Ref[PublicSubnet2RouteTable] = ref()
    depends_on = ["VPCGW"]
