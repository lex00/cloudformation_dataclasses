"""PublicSubnetRouteTableAssociation0 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnetRouteTableAssociation0:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    subnet_id = ref(PublicSubnet0)
    route_table_id = ref(PublicRouteTable)
