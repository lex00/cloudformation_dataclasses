from __future__ import annotations

"""PrivateSubnetRouteTableAssociation1 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnetRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    subnet_id: Ref[PrivateSubnet1] = ref()
    route_table_id: Ref[PrivateRouteTable1] = ref()
