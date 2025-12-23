"""NATGateway1 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway1:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(EIP1, "AllocationId")
    subnet_id = ref(PublicSubnet1)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-nat-gw1'),
    }]
