from __future__ import annotations

"""NetworkInternetGateway - AWS::EC2::InternetGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkInternetGatewayAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'vscode-server'


@cloudformation_dataclass
class NetworkInternetGateway:
    """AWS::EC2::InternetGateway resource."""

    resource: InternetGateway
    tags = [NetworkInternetGatewayAssociationParameter]
