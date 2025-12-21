from __future__ import annotations

"""PrivateLoadBalancerIngressFromECS - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateLoadBalancerIngressFromECS:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    description = 'Only accept traffic from a container in the fargate container security group'
    group_id: Ref[PrivateLoadBalancerSG] = ref()
    ip_protocol = '-1'
    source_security_group_id: Ref[FargateContainerSecurityGroup] = ref()
