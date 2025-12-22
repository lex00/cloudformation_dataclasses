from __future__ import annotations

"""PrivateRouteTableAssociation1 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PrivateRouteTable1] = ref()
    subnet_id: Ref[PrivateSubnet1] = ref()
