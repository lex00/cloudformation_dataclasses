"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EIP1:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class EIP2:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class ENI:
    """AWS::EC2::NetworkInterface resource."""

    resource: ec2.NetworkInterface
    secondary_private_ip_address_count = 2
    source_dest_check = True
    subnet_id = Select(0, ref(Subnet))


@cloudformation_dataclass
class Association1:
    """AWS::EC2::EIPAssociation resource."""

    resource: ec2.EIPAssociation
    allocation_id = get_att(EIP1, "AllocationId")
    network_interface_id = ref(ENI)
    private_ip_address = Select(0, get_att(ENI, "SecondaryPrivateIpAddresses"))
    depends_on = ["ENI", "EIP1"]


@cloudformation_dataclass
class Association2:
    """AWS::EC2::EIPAssociation resource."""

    resource: ec2.EIPAssociation
    allocation_id = get_att(EIP2, "AllocationId")
    network_interface_id = ref(ENI)
    private_ip_address = Select(1, get_att(ENI, "SecondaryPrivateIpAddresses"))
    depends_on = ["ENI", "EIP2"]
