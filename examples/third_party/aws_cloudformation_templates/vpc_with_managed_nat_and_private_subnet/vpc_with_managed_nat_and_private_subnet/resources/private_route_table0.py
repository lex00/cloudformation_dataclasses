from __future__ import annotations

"""PrivateRouteTable0 - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTable0AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-private-route-table-0',
])


@cloudformation_dataclass
class PrivateRouteTable0:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[VPC] = ref()
    tags = [PrivateRouteTable0AssociationParameter]
