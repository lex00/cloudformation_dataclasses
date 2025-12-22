from __future__ import annotations

"""PrivateSubnet1RouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PrivateRouteTable1] = ref()
    subnet_id: Ref[PrivateSubnet1] = ref()
