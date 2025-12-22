"""PrivateRouteTable1 - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTable1AssociationParameter:
    resource: ec2.instance.AssociationParameter
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
