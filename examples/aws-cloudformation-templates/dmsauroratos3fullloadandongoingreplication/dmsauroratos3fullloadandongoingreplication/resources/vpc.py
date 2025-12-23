"""VPC - AWS::EC2::VPC resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPC:
    """AWS::EC2::VPC resource."""

    resource: ec2.VPC
    cidr_block = '10.0.0.0/24'
    enable_dns_support = 'true'
    enable_dns_hostnames = 'true'
    tags = [{
        'Key': 'Application',
        'Value': AWS_STACK_ID,
    }, {
        'Key': 'Name',
        'Value': AWS_STACK_NAME,
    }]
