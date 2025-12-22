from __future__ import annotations

"""PrivateRouteTable3 - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTable3AssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-private-route-table3')


@cloudformation_dataclass
class PrivateRouteTable3:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[VPC] = ref()
    tags = [PrivateRouteTable3AssociationParameter]
