from __future__ import annotations

"""AttachGateway - AWS::EC2::VPCGatewayAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AttachGateway:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: VPCGatewayAttachment
    vpc_id: Ref[VPC] = ref()
    internet_gateway_id: Ref[InternetGateway] = ref()
