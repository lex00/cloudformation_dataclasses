"""PrivateSubnet0 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet0AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PrivateSubnet0AssociationParameter1:
    resource: ec2.instance.AssociationParameter
    key = 'Network'
    value = 'Private'


@cloudformation_dataclass
class PrivateSubnet0AssociationParameter2:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-private-',
    Select(0, GetAZs()),
])


@cloudformation_dataclass
class PrivateSubnet0:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs())
    cidr_block = FindInMap("SubnetConfig", 'Private0', 'CIDR')
    tags = [PrivateSubnet0AssociationParameter, PrivateSubnet0AssociationParameter1, PrivateSubnet0AssociationParameter2]
