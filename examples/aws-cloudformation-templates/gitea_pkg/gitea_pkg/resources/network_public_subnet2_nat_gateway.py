"""NetworkPublicSubnet2NATGateway - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2NATGatewayAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitea-server-public-subnet-ngw'


@cloudformation_dataclass
class NetworkPublicSubnet2NATGateway:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(NetworkPublicSubnet2EIP, "AllocationId")
    subnet_id = ref(NetworkPublicSubnet2)
    tags = [NetworkPublicSubnet2NATGatewayAssociationParameter]
    depends_on = ["NetworkPublicSubnet2DefaultRoute", "NetworkPublicSubnet2RouteTableAssociation"]
