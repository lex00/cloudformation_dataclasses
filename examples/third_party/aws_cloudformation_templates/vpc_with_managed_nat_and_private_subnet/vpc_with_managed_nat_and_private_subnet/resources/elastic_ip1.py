from __future__ import annotations

"""ElasticIP1 - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ElasticIP1:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
