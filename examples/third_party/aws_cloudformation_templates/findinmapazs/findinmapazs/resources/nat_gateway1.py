from __future__ import annotations

"""NatGateway1 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[NatGateway1EIP] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnet1] = ref()
