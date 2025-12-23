"""Network resources: EIP1, EIP2, ENI."""

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
