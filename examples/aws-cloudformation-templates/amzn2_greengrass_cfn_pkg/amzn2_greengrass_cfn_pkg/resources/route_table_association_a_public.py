"""RouteTableAssociationAPublic - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class RouteTableAssociationAPublic:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: SubnetRouteTableAssociation
    route_table_id = ref(RouteTablePublic)
    subnet_id = ref(SubnetAPublic)
