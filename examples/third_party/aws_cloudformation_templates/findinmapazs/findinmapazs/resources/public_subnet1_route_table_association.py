from __future__ import annotations

"""PublicSubnet1RouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PublicRouteTable] = ref()
    subnet_id: Ref[PublicSubnet1] = ref()
