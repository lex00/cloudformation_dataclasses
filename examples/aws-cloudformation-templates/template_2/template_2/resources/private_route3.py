"""PrivateRoute3 - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRoute3:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable3)
    nat_gateway_id = ref(NATGateway3)
    destination_cidr_block = '0.0.0.0/0'
