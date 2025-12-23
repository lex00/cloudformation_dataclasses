"""EIPAssoc1 - AWS::EC2::EIPAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EIPAssoc1:
    """AWS::EC2::EIPAssociation resource."""

    resource: ec2.EIPAssociation
    network_interface_id = ref(Eth0)
    allocation_id = get_att(EIP1, "AllocationId")
