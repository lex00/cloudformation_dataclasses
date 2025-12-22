from __future__ import annotations

"""PrivateRouteTable2 - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTable2AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table2')


@cloudformation_dataclass
class PrivateRouteTable2:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[VPC] = ref()
    tags = [PrivateRouteTable2AssociationParameter]
