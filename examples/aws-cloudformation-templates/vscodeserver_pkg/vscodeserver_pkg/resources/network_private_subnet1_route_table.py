"""NetworkPrivateSubnet1RouteTable - AWS::EC2::RouteTable resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTableAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'vscode-server-private-subnet-1-rt'


@cloudformation_dataclass
class NetworkPrivateSubnet1RouteTable:
    """AWS::EC2::RouteTable resource."""

    resource: ec2.RouteTable
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPrivateSubnet1RouteTableAssociationParameter]
