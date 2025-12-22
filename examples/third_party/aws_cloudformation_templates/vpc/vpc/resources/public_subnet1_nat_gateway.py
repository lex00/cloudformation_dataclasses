from __future__ import annotations

"""PublicSubnet1NATGateway - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[PublicSubnet1EIP] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnet1] = ref()
    depends_on = ["PublicSubnet1DefaultRoute", "PublicSubnet1RouteTableAssociation"]
