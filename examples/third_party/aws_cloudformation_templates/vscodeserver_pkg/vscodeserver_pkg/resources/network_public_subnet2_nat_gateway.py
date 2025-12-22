from __future__ import annotations

"""NetworkPublicSubnet2NATGateway - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2NATGatewayAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'vscode-server-public-subnet-ngw'


@cloudformation_dataclass
class NetworkPublicSubnet2NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[NetworkPublicSubnet2EIP] = get_att("AllocationId")
    subnet_id: Ref[NetworkPublicSubnet2] = ref()
    tags = [NetworkPublicSubnet2NATGatewayAssociationParameter]
    depends_on = ["NetworkPublicSubnet2DefaultRoute", "NetworkPublicSubnet2RouteTableAssociation"]
