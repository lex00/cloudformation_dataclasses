from __future__ import annotations

"""PublicSubnet3 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet3AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet3')


@cloudformation_dataclass
class PublicSubnet3AssociationParameter1:
    resource: AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


@cloudformation_dataclass
class PublicSubnet3:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(2, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = ref(PublicCidrBlock3)
    tags = [PublicSubnet3AssociationParameter, PublicSubnet3AssociationParameter1]
