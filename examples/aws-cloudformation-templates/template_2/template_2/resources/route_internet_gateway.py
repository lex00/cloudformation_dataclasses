"""RouteInternetGateway - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RouteInternetGateway:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PublicRouteTable)
    gateway_id = ref(InternetGateway)
    destination_cidr_block = '0.0.0.0/0'
