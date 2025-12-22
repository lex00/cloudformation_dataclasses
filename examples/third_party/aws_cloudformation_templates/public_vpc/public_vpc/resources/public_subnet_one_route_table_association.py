from __future__ import annotations

"""PublicSubnetOneRouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetOneRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    subnet_id: Ref[PublicSubnetOne] = ref()
    route_table_id: Ref[PublicRouteTable] = ref()
