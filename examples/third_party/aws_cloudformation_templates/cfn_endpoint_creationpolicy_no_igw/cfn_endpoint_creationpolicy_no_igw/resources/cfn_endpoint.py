from __future__ import annotations

"""CfnEndpoint - AWS::EC2::VPCEndpoint resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CfnEndpoint:
    """AWS::EC2::VPCEndpoint resource."""

    resource: VPCEndpoint
    vpc_id: Ref[VPC] = ref()
    service_name = Sub('com.amazonaws.${AWS::Region}.cloudformation')
    vpc_endpoint_type = 'Interface'
    private_dns_enabled = True
    subnet_ids = [ref("PrivateSubnet1"), ref("PrivateSubnet2")]
    security_group_ids = [ref("EndpointSG")]
