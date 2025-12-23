"""NetworkPrivateSubnet1Subnet - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NetworkPrivateSubnet1SubnetAssociationParameter:
    resource: ec2.instance.AssociationParameter
    key = 'Name'
    value = 'gitlab-server-private-subnet-1'


@cloudformation_dataclass
class NetworkPrivateSubnet1Subnet:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = '10.0.128.0/18'
    map_public_ip_on_launch = False
    vpc_id = ref(NetworkVPC)
    tags = [NetworkPrivateSubnet1SubnetAssociationParameter]
