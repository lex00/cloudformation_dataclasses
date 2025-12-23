"""NetworkPublicSubnet1RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-rt'


@cloudformation_dataclass
class NetworkPublicSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPublicSubnet1RouteTableAssociationParameter]
