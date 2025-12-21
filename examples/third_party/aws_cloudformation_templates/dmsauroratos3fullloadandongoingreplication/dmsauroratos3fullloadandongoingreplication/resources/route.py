from __future__ import annotations

"""Route - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Route:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id: Ref[RouteTable] = ref()
    destination_cidr_block = '0.0.0.0/0'
    gateway_id: Ref[InternetGateway] = ref()
    depends_on = ["AttachGateway"]
