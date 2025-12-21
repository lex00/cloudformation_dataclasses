from __future__ import annotations

"""NatGateway2 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGateway2:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[NatGateway2EIP] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnet2] = ref()
