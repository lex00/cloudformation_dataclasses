from __future__ import annotations

"""EIP3 - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EIP3:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
