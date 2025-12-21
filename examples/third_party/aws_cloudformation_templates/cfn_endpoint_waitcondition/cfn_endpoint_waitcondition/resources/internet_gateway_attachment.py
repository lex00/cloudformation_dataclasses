from __future__ import annotations

"""InternetGatewayAttachment - AWS::EC2::VPCGatewayAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InternetGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: VPCGatewayAttachment
    internet_gateway_id: Ref[InternetGateway] = ref()
    vpc_id: Ref[VPC] = ref()
