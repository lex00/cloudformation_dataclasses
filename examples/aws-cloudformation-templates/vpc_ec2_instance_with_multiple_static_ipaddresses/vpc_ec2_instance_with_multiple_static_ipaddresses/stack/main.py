"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EIP1:
    """AWS::EC2::EIP resource."""

    resource: ec2.EIP
    domain = 'vpc'


@cloudformation_dataclass
class SSHSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class SSHSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    vpc_id = ref(VpcId)
    group_description = 'Enable SSH access via port 22'
    security_group_ingress = [SSHSecurityGroupEgress]


@cloudformation_dataclass
class Eth0PrivateIpAddressSpecification:
    resource: ec2.instance.PrivateIpAddressSpecification
    private_ip_address = ref(PrimaryIPAddress)
    primary = 'true'


@cloudformation_dataclass
class Eth0PrivateIpAddressSpecification1:
    resource: ec2.instance.PrivateIpAddressSpecification
    private_ip_address = ref(SecondaryIPAddress)
    primary = 'false'


@cloudformation_dataclass
class Eth0AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'Interface 0'


@cloudformation_dataclass
class Eth0AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Interface'
    value = 'eth0'


@cloudformation_dataclass
class Eth0:
    """AWS::EC2::NetworkInterface resource."""

    resource: ec2.NetworkInterface
    description = 'eth0'
    group_set = [ref(SSHSecurityGroup)]
    private_ip_addresses = [Eth0PrivateIpAddressSpecification, Eth0PrivateIpAddressSpecification1]
    source_dest_check = 'true'
    subnet_id = ref(SubnetId)
    tags = [Eth0AssociationParameter, Eth0AssociationParameter1]


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
