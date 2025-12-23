"""NatGatewayTwo - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGatewayTwo:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NatGatewayTwoAttachment, "AllocationId")
    subnet_id = ref(PublicSubnetTwo)
