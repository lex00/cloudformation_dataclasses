"""NatGateway2EIP - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGateway2EIP:
    """AWS::EC2::EIP resource."""

    resource: EIP
    domain = 'vpc'
    depends_on = ["InternetGatewayAttachment"]
