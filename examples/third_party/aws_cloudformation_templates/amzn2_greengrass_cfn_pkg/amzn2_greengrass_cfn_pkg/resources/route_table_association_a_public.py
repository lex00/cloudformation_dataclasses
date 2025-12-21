from __future__ import annotations

"""RouteTableAssociationAPublic - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RouteTableAssociationAPublic:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[RouteTablePublic] = ref()
    subnet_id: Ref[SubnetAPublic] = ref()
