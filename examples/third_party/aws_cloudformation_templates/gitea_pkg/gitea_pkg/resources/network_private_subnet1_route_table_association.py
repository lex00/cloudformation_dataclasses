from __future__ import annotations

"""NetworkPrivateSubnet1RouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[NetworkPrivateSubnet1RouteTable] = ref()
    subnet_id: Ref[NetworkPrivateSubnet1Subnet] = ref()
