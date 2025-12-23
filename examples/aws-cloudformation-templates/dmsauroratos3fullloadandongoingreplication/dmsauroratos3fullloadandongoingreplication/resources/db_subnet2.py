"""DBSubnet2 - AWS::EC2::Subnet resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DBSubnet2:
    """AWS::EC2::Subnet resource."""

    resource: ec2.Subnet
    vpc_id = ref(VPC)
    cidr_block = '10.0.0.64/26'
    availability_zone = Select(1, GetAZs())
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }]
