from __future__ import annotations

"""NetworkVPCGW - AWS::EC2::VPCGatewayAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkVPCGW:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: VPCGatewayAttachment
    internet_gateway_id: Ref[NetworkInternetGateway] = ref()
    vpc_id: Ref[NetworkVPC] = ref()
