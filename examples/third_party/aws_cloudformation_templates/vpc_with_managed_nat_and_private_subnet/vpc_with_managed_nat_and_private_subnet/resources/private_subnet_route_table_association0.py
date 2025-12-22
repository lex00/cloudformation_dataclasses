from __future__ import annotations

"""PrivateSubnetRouteTableAssociation0 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnetRouteTableAssociation0:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    subnet_id: Ref[PrivateSubnet0] = ref()
    route_table_id: Ref[PrivateRouteTable0] = ref()
