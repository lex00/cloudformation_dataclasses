"""SubnetRouteTableAssociation1 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SubnetRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    subnet_id = ref(DBSubnet2)
    route_table_id = ref(RouteTable)
