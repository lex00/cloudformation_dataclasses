from __future__ import annotations

"""NetworkPrivateSubnet2Subnet - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet2SubnetAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'vscode-server-private-subnet-2'


@cloudformation_dataclass
class NetworkPrivateSubnet2Subnet:
    """AWS::EC2::Subnet resource."""

    resource: Subnet
    availability_zone = Select(1, GetAZs({'Ref': 'AWS::Region'}))
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id: Ref[NetworkVPC] = ref()
    tags = [NetworkPrivateSubnet2SubnetAssociationParameter]
