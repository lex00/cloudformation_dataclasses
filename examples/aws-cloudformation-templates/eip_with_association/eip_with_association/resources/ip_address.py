"""IPAddress - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class IPAddress:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
