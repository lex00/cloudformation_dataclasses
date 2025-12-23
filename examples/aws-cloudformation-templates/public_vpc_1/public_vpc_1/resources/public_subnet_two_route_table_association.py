"""PublicSubnetTwoRouteTableAssociation - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetTwoRouteTableAssociation:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnetTwo)
    route_table_id = ref(PublicRouteTable)
