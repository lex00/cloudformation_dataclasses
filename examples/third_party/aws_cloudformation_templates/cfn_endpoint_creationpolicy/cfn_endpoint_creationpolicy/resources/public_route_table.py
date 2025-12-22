"""PublicRouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicRouteTableAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = Sub('${EnvironmentName} Public Routes')


@cloudformation_dataclass
class PublicRouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: RouteTable
    vpc_id = ref(VPC)
    tags = [PublicRouteTableAssociationParameter]
