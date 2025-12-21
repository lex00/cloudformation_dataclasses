from __future__ import annotations

"""PrivateRouteTableAssociation3 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTableAssociation3:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PrivateRouteTable3] = ref()
    subnet_id: Ref[PrivateSubnet3] = ref()
