from __future__ import annotations

"""NetworkPrivateSubnet2RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet2RouteTableAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-2-rt'


@cloudformation_dataclass
class NetworkPrivateSubnet2RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[NetworkVPC] = ref()
    tags = [NetworkPrivateSubnet2RouteTableAssociationParameter]
