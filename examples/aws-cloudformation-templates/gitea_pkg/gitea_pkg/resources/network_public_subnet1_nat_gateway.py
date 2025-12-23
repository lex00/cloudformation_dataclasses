"""NetworkPublicSubnet1NATGateway - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet1NATGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitea-server-public-subnet-1-ngw'


@cloudformation_dataclass
class NetworkPublicSubnet1NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NetworkPublicSubnet1EIP, "AllocationId")
    subnet_id = ref(NetworkPublicSubnet1)
    tags = [NetworkPublicSubnet1NATGatewayAssociationParameter]
    depends_on = ["NetworkPublicSubnet1DefaultRoute", "NetworkPublicSubnet1RouteTableAssociation"]
