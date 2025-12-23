"""Association2 - AWS::EC2::EIPAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Association2:
    """AWS::EC2::EIPAssociation resource."""

    resource: ec2.EIPAssociation
    allocation_id = get_att(EIP2, "AllocationId")
    network_interface_id = ref(ENI)
    private_ip_address = Select(1, get_att(ENI, "SecondaryPrivateIpAddresses"))
    depends_on = ["ENI", "EIP2"]
