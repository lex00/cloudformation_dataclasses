from __future__ import annotations

"""SubnetRouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SubnetRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id: Ref[DBSubnet1] = ref()
    route_table_id: Ref[RouteTable] = ref()
