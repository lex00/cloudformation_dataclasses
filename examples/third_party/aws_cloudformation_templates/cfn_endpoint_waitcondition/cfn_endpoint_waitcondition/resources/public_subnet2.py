from __future__ import annotations

"""PublicSubnet2 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet2AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Public Subnet (AZ2)')


@cloudformation_dataclass
class PublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = ref(PublicSubnet2CIDR)
    map_public_ip_on_launch = True
    tags = [PublicSubnet2AssociationParameter]
