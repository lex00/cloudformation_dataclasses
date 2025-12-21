from __future__ import annotations

"""NetworkPublicSubnet1RouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[NetworkPublicSubnet1RouteTable] = ref()
    subnet_id: Ref[NetworkPublicSubnet1] = ref()
