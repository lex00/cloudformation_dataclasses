from __future__ import annotations

"""PublicRouteTableAssociation1 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicRouteTableAssociation1:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PublicRouteTable] = ref()
    subnet_id: Ref[PublicSubnet1] = ref()
