"""PrivateSubnet2DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet2DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(PublicSubnet2NATGateway)
    route_table_id = ref(PrivateSubnet2RouteTable)
