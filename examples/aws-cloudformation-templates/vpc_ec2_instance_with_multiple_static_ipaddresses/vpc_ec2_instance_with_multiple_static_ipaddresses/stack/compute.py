"""Compute resources: EIPAssoc1, EC2Instance."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EIPAssoc1:
    """AWS::EC2::EIPAssociation resource."""

    resource: ec2.EIPAssociation
    network_interface_id = ref(Eth0)
    allocation_id = get_att(EIP1, "AllocationId")


@cloudformation_dataclass
class EC2InstanceInstanceNetworkInterfaceSpecification:
    resource: ec2.spot_fleet.InstanceNetworkInterfaceSpecification
    network_interface_id = ref(Eth0)
    device_index = '0'


@cloudformation_dataclass
class EC2InstanceAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'myInstance'


@cloudformation_dataclass
class EC2Instance:
    """AWS::EC2::Instance resource."""

    resource: ec2.Instance
    image_id = ref(LatestAMI)
    instance_type = ref(InstanceType)
    key_name = ref(KeyName)
    network_interfaces = [EC2InstanceInstanceNetworkInterfaceSpecification]
    tags = [EC2InstanceAssociationParameter]
