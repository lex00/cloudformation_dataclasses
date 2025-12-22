from __future__ import annotations

"""NetworkPublicSubnet2RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2RouteTableAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitea-server-public-subnet-2-rt'


@cloudformation_dataclass
class NetworkPublicSubnet2RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[NetworkVPC] = ref()
    tags = [NetworkPublicSubnet2RouteTableAssociationParameter]
