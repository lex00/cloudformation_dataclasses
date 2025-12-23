"""PrivateSubnetTwo - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnetTwo:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    availability_zone = Select(1, GetAZs(AWS_REGION))
    vpc_id = ref(VPC)
    cidr_block = FindInMap("SubnetConfig", 'PrivateTwo', 'CIDR')
