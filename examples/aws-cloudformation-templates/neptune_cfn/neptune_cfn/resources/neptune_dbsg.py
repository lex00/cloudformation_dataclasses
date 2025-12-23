"""NeptuneDBSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneDBSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'SG of Neptune DB'
    vpc_id = ImportValue(Sub('${VPCStack}-VPCID'))
    tags = [{
        'Key': 'Name',
        'Value': Sub('${AWS::StackName}-neptune-sg'),
    }]
