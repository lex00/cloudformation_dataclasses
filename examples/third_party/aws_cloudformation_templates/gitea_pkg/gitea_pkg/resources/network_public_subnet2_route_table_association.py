from __future__ import annotations

"""NetworkPublicSubnet2RouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[NetworkPublicSubnet2RouteTable] = ref()
    subnet_id: Ref[NetworkPublicSubnet2] = ref()
