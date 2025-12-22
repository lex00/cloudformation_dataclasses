from __future__ import annotations

"""PublicSubnet1NATGateway - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id = get_att(PublicSubnet1EIP, "AllocationId")
    subnet_id = ref(PublicSubnet1)
    depends_on = ["PublicSubnet1DefaultRoute", "PublicSubnet1RouteTableAssociation"]
