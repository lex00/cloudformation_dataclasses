"""VPCGatewayAttachment - AWS::EC2::VPCGatewayAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(InternetGateway)
    vpc_id = ref(VPC)
