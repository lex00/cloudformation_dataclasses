"""Compute resources: LoadBalancerEgress."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerEgress:
    """AWS::EC2::SecurityGroupEgress resource."""

    resource: ec2.SecurityGroupEgress
    description = 'Load balancer to target'
    destination_security_group_id = ref(DestinationSecurityGroupId)
    from_port = 80
    group_id = get_att(LoadBalancerSecurityGroup, "GroupId")
    ip_protocol = 'tcp'
    to_port = 80
