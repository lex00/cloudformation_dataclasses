"""FirstEIP - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class FirstEIP:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
