from __future__ import annotations

"""PublicSubnetTwoRouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetTwoRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    subnet_id: Ref[PublicSubnetTwo] = ref()
    route_table_id: Ref[PublicRouteTable] = ref()
