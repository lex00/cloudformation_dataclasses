"""PublicSubnet1 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicSubnet1:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    availability_zone = Select(0, GetAZs(AWS_REGION))
    cidr_block = ref(PublicCidrBlock1)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-public-subnet1'),
    }, {
        'Key': 'kubernetes.io/role/elb',
        'Value': 1,
    }]
