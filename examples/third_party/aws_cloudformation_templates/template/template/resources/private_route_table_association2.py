from __future__ import annotations

"""PrivateRouteTableAssociation2 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTableAssociation2:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PrivateRouteTable2] = ref()
    subnet_id: Ref[PrivateSubnet2] = ref()
