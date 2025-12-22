"""EC2Instance - AWS::EC2::Instance resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2InstanceNetworkInterface:
    resource: ec2.NetworkInterface
    network_interface_id = ref(Eth0)
    device_index = '0'


@cloudformation_dataclass
class EC2InstanceAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'myInstance'


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(LatestAMI)
    instance_type = ref(InstanceType)
    key_name = ref(KeyName)
    network_interfaces = [EC2InstanceNetworkInterface]
    tags = [EC2InstanceAssociationParameter]
