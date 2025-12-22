from __future__ import annotations

"""PublicRouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicRouteTableAssociationParameter:
    resource: AssociationParameter
    key = 'Application'
    value = AWS_STACK_NAME


@cloudformation_dataclass
class PublicRouteTableAssociationParameter1:
    resource: AssociationParameter
    key = 'Network'
    value = 'Public'


@cloudformation_dataclass
class PublicRouteTableAssociationParameter2:
    resource: AssociationParameter
    key = 'Name'
    value = Join('', [
    ref(VPCName),
    '-public-route-table',
])


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id = ref(VPC)
    tags = [PublicRouteTableAssociationParameter, PublicRouteTableAssociationParameter1, PublicRouteTableAssociationParameter2]
