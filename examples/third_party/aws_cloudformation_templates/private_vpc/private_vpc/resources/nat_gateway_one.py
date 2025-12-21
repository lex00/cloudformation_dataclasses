from __future__ import annotations

"""NatGatewayOne - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGatewayOne:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[NatGatewayOneAttachment] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnetOne] = ref()
