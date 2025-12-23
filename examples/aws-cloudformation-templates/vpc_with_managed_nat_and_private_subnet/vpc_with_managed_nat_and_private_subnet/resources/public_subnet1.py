"""PublicSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicSubnet1AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicSubnet1AssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-',
    Select(1, GetAZs()),
])


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Public1', 'CIDR')
    map_public_ip_on_launch = 'true'
    tags = [PublicSubnet1AssociationParameter, PublicSubnet1AssociationParameter1, PublicSubnet1AssociationParameter2]
