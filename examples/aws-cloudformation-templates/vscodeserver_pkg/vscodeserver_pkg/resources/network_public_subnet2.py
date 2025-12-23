"""NetworkPublicSubnet2 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPublicSubnet2AssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'vscode-server-public-subnet-2'


@cloudformation_dataclass
class NetworkPublicSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = '10.0.64.0/18'
    map_public_ip_on_launch = True
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPublicSubnet2AssociationParameter]
