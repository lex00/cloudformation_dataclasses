"""EcsHostSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EcsHostSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the ECS hosts that run containers'
    vpc_id = ref(VPC)
