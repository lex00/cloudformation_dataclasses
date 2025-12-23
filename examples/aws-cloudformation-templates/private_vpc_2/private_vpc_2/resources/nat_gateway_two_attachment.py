"""NatGatewayTwoAttachment - AWS::EC2::EIP resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGatewayTwoAttachment:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'
    depends_on = ["GatewayAttachement"]
