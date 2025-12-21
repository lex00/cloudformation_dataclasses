from __future__ import annotations

"""NatGateway1EIP - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGateway1EIP:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
    depends_on = ["InternetGatewayAttachment"]
