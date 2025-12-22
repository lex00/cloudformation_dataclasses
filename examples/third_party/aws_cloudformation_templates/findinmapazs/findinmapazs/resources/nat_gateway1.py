from __future__ import annotations

"""NatGateway1 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id = get_att(NatGateway1EIP, "AllocationId")
    subnet_id = ref(PublicSubnet1)
