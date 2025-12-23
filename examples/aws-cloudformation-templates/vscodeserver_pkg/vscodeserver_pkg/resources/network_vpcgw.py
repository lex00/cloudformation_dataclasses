"""NetworkVPCGW - AWS::EC2::VPCGatewayAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkVPCGW:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id = ref(NetworkInternetGateway)
    vpc_id = ref(NetworkVPC)
