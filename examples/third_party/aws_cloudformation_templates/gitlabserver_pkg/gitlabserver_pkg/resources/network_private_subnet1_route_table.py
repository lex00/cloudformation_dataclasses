from __future__ import annotations

"""NetworkPrivateSubnet1RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTableAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-1-rt'


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[NetworkVPC] = ref()
    tags = [NetworkPrivateSubnet1RouteTableAssociationParameter]
