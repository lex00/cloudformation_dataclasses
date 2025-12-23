"""NetworkPublicSubnet2RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2RouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'vscode-server-public-subnet-2-rt'


@cloudformation_dataclass
class NetworkPublicSubnet2RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPublicSubnet2RouteTableAssociationParameter]
