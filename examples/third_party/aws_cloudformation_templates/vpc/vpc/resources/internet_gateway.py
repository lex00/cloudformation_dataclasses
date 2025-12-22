from __future__ import annotations

"""InternetGateway - AWS::EC2::InternetGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
