"""NatGateway2 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NatGateway2:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id = get_att(NatGateway2EIP, "AllocationId")
    subnet_id = ref(PublicSubnet2)
