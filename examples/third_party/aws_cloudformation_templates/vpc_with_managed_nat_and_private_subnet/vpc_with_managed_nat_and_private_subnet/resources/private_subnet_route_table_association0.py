from __future__ import annotations

"""PrivateSubnetRouteTableAssociation0 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnetRouteTableAssociation0:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    subnet_id = ref(PrivateSubnet0)
    route_table_id = ref(PrivateRouteTable0)
