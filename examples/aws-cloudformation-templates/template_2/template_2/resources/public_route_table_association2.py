"""PublicRouteTableAssociation2 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicRouteTableAssociation2:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PublicRouteTable)
    subnet_id = ref(PublicSubnet2)
