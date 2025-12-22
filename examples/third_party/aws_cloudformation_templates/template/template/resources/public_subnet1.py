from __future__ import annotations

"""PublicSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet1')


@cloudformation_dataclass
class PublicSubnet1AssociationParameter1:
    resource: AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(0, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = ref(PublicCidrBlock1)
    tags = [PublicSubnet1AssociationParameter, PublicSubnet1AssociationParameter1]
