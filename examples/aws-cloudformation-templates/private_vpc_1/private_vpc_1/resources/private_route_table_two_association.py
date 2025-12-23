"""PrivateRouteTableTwoAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTableTwoAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTableTwo)
    subnet_id = ref(PrivateSubnetTwo)
