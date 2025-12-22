from __future__ import annotations

"""PublicSubnetRouteTableAssociation1 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    subnet_id: Ref[PublicSubnet1] = ref()
    route_table_id: Ref[PublicRouteTable] = ref()
