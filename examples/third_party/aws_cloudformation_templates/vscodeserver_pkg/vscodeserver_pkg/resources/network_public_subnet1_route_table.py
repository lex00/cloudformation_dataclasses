from __future__ import annotations

"""NetworkPublicSubnet1RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTableAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'vscode-server-public-subnet-1-rt'


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[NetworkVPC] = ref()
    tags = [NetworkPublicSubnet1RouteTableAssociationParameter]
