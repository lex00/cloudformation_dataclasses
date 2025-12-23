"""ENI - AWS::EC2::NetworkInterface resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ENI:
    """AWS::EC2::NetworkInterface resource."""

    resource: ec2.NetworkInterface
    secondary_private_ip_address_count = 2
    source_dest_check = True
    subnet_id = Select(0, ref(Subnet))
