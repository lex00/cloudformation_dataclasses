"""PrivateRouteTableAssociation2 - AWS::EC2::SubnetRouteTableAssociation resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateRouteTableAssociation2:
    """AWS::EC2::SubnetRouteTableAssociation resource."""

    resource: ec2.SubnetRouteTableAssociation
    route_table_id = ref(PrivateRouteTable2)
    subnet_id = ref(PrivateSubnet2)
