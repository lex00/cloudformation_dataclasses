from __future__ import annotations

"""NatGatewayOneAttachment - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGatewayOneAttachment:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
    depends_on = ["GatewayAttachement"]
