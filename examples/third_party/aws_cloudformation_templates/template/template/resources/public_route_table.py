from __future__ import annotations

"""PublicRouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicRouteTableAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${AWS::StackName}-public-route-table')


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id: Ref[VPC] = ref()
    tags = [PublicRouteTableAssociationParameter]
