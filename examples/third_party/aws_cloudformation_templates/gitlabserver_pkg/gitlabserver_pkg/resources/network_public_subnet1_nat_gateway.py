from __future__ import annotations

"""NetworkPublicSubnet1NATGateway - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1NATGatewayAssociationParameter:
    resource: AssociationParameter
    key = 'Name'
    value = 'gitlab-server-public-subnet-1-ngw'


@cloudformation_dataclass
class NetworkPublicSubnet1NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: NatGateway
    allocation_id: GetAtt[NetworkPublicSubnet1EIP] = get_att("AllocationId")
    subnet_id: Ref[NetworkPublicSubnet1] = ref()
    tags = [NetworkPublicSubnet1NATGatewayAssociationParameter]
    depends_on = ["NetworkPublicSubnet1DefaultRoute", "NetworkPublicSubnet1RouteTableAssociation"]
