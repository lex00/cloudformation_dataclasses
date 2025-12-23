"""NATGateway2 - AWS::EC2::NatGateway resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NATGateway2:
    """AWS::EC2::NatGateway resource."""

    resource: ec2.NatGateway
    allocation_id = get_att(EIP2, "AllocationId")
    subnet_id = ref(PublicSubnet2)
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-nat-gw2'),
    }]
