"""NATGateway1 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(ElasticIP1, "AllocationId")
    subnet_id = ref(PublicSubnet1)
