"""NetworkInternetGateway - AWS::EC2::InternetGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkInternetGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitea-server'


@cloudformation_dataclass
class NetworkInternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: ec2.InternetGateway
    tags = [NetworkInternetGatewayAssociationParameter]
