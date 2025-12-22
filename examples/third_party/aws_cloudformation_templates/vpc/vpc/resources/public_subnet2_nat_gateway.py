from __future__ import annotations

"""PublicSubnet2NATGateway - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet2NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id = get_att(PublicSubnet2EIP, "AllocationId")
    subnet_id = ref(PublicSubnet2)
    depends_on = ["PublicSubnet2DefaultRoute", "PublicSubnet2RouteTableAssociation"]
