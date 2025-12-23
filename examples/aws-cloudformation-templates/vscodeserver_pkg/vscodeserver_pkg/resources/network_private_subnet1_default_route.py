"""NetworkPrivateSubnet1DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet1DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NetworkPublicSubnet1NATGateway)
    route_table_id = ref(NetworkPrivateSubnet1RouteTable)
