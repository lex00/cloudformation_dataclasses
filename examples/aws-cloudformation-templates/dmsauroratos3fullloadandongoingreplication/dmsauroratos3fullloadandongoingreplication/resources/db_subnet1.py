"""DBSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DBSubnet1AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Application'
    value = AWS_STACK_ID


@cloudformation_dataclass
class DBSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id = ref(VPC)
    cidr_block = '10.0.0.0/26'
    availability_zone = Select(0, GetAZs())
    tags = [DBSubnet1AssociationParameter]
