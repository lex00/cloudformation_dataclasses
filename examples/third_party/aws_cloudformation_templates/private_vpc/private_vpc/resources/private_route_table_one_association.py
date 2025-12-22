from __future__ import annotations

"""PrivateRouteTableOneAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTableOneAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PrivateRouteTableOne] = ref()
    subnet_id: Ref[PrivateSubnetOne] = ref()
