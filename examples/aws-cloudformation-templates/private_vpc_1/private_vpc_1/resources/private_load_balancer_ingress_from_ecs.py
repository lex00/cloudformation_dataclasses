"""PrivateLoadBalancerIngressFromECS - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateLoadBalancerIngressFromECS:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: ec2.SecurityGroupIngress
    description = 'Only accept traffic from a container in the container host security group'
    group_id = ref(PrivateLoadBalancerSG)
    ip_protocol = -1
    source_security_group_id = ref(EcsHostSecurityGroup)
