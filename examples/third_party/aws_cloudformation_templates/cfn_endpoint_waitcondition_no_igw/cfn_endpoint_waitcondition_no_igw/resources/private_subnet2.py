from __future__ import annotations

"""PrivateSubnet2 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet2AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Subnet (AZ2)')


@cloudformation_dataclass
class PrivateSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(1, GetAZs())
    cidr_block = ref(PrivateSubnet2CIDR)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet2AssociationParameter]
