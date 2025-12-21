from __future__ import annotations

"""PublicRouteTableAssociation3 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicRouteTableAssociation3:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id: Ref[PublicRouteTable] = ref()
    subnet_id: Ref[PublicSubnet3] = ref()
