"""PrivateRouteToInternet1 - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteToInternet1:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTable1)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NATGateway1)
