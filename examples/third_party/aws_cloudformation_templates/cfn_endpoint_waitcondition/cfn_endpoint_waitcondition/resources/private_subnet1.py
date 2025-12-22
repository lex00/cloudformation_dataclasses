from __future__ import annotations

"""PrivateSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet1AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Private Subnet (AZ1)')


@cloudformation_dataclass
class PrivateSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs())
    cidr_block = ref(PrivateSubnet1CIDR)
    map_public_ip_on_launch = False
    tags = [PrivateSubnet1AssociationParameter]
