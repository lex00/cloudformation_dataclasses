from __future__ import annotations

"""PublicSubnet2 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet2AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-subnet2')


@cloudformation_dataclass
class PublicSubnet2AssociationParameter1:
    resource: AssociationParameter
    key = 'kubernetes.io/role/elb'
    value = 1


@cloudformation_dataclass
class PublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id: Ref[VPC] = ref()
    availability_zone = Select(1, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = ref(PublicCidrBlock2)
    tags = [PublicSubnet2AssociationParameter, PublicSubnet2AssociationParameter1]
