from __future__ import annotations

"""PrivateRouteTableTwoAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTableTwoAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PrivateRouteTableTwo] = ref()
    subnet_id: Ref[PrivateSubnetTwo] = ref()
