"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class VPCOutput:
    """A reference to the created VPC"""

    resource: Output
    value = ref("VPC")
    description = 'A reference to the created VPC'


@cloudformation_dataclass
class PrivateSubnetsOutput:
    """A list of the private subnets"""

    resource: Output
    value = Join(',', [
    ref("PrivateSubnet1"),
    ref("PrivateSubnet2"),
])
    description = 'A list of the private subnets'


@cloudformation_dataclass
class CfnEndpointOutput:
    """A reference to the CloudFormation Endpoint used for signaling from the private instance"""

    resource: Output
    value = ref("CfnEndpoint")
    description = 'A reference to the CloudFormation Endpoint used for signaling from the private instance'
