"""NetworkPrivateSubnet1RouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(NetworkPrivateSubnet1RouteTable)
    subnet_id = ref(NetworkPrivateSubnet1Subnet)
