from __future__ import annotations

"""NatGatewayTwo - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGatewayTwo:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[NatGatewayTwoAttachment] = get_att("AllocationId")
    subnet_id: Ref[PublicSubnetTwo] = ref()
