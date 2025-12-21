from __future__ import annotations

"""VPCGatewayAttachment - AWS::EC2::VPCGatewayAttachment resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCGatewayAttachment:
    """AWS::EC2::VPCGatewayAttachment resource."""

    resource: ec2.VPCGatewayAttachment
    internet_gateway_id: Ref[InternetGateway] = ref()
    vpc_id: Ref[VPC] = ref()
