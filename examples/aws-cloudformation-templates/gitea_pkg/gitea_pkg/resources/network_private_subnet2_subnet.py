"""NetworkPrivateSubnet2Subnet - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet2SubnetAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitea-server-private-subnet-2'


@cloudformation_dataclass
class NetworkPrivateSubnet2Subnet:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    cidr_block = '10.0.192.0/18'
    map_public_ip_on_launch = False
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPrivateSubnet2SubnetAssociationParameter]
