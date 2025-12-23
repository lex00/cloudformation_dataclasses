"""PrivateRouteOne - AWS::EC2::Route resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteOne:
    """AWS::EC2::Route resource."""

    resource: ec2.Route
    route_table_id = ref(PrivateRouteTableOne)
    destination_cidr_block = '0.0.0.0/0'
    nat_gateway_id = ref(NatGatewayOne)
