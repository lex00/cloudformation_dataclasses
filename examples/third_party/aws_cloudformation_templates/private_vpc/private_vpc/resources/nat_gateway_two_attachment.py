from __future__ import annotations

"""NatGatewayTwoAttachment - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGatewayTwoAttachment:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
    depends_on = ["GatewayAttachement"]
