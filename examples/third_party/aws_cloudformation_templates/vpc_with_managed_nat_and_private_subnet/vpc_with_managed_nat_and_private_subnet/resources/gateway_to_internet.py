"""GatewayToInternet - AWS::EC2::VPCGatewayAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GatewayToInternet:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: VPCGatewayAttachment
    vpc_id = ref(VPC)
    internet_gateway_id = ref(InternetGateway)
