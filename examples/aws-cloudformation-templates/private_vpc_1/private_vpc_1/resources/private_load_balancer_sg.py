"""PrivateLoadBalancerSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateLoadBalancerSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the internal load balancer'
    vpc_id = ref(VPC)
