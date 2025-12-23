"""NetworkPublicSubnet1DefaultRoute - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1DefaultRoute:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    destination_cidr_block = '0.0.0.0/0'
    gateway_id = ref(NetworkInternetGateway)
    route_table_id = ref(NetworkPublicSubnet1RouteTable)
    depends_on = ["NetworkVPCGW"]
