"""NetworkPublicSubnet1RouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(NetworkPublicSubnet1RouteTable)
    subnet_id = ref(NetworkPublicSubnet1)
