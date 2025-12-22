from __future__ import annotations

"""PublicSubnet1EIP - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1EIP:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
