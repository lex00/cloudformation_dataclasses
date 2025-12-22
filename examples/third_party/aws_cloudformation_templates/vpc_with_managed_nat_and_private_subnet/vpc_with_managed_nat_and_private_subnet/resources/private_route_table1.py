from __future__ import annotations

"""PrivateRouteTable1 - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTable1AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-private-route-table-1',
])


@cloudformation_dataclass
class PrivateRouteTable1:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id = ref(VPC)
    tags = [PrivateRouteTable1AssociationParameter]
