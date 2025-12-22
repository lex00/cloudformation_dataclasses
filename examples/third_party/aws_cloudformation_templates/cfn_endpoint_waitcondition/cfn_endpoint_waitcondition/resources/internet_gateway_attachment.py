"""InternetGatewayAttachment - AWS::EC2::VPCGatewayAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InternetGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)
