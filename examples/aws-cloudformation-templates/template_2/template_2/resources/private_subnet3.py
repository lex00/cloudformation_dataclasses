"""PrivateSubnet3 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateSubnet3:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(2, GetAZs(AWS_REGION))
    cidr_block = ref(PrivateCidrBlock3)
    map_public_ip_on_launch = False
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-private-subnet3'),
    }]
