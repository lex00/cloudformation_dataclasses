from __future__ import annotations

"""EcsSecurityGroupIngressFromPrivateALB - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EcsSecurityGroupIngressFromPrivateALB:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    description = 'Ingress from the private ALB'
    group_id: Ref[FargateContainerSecurityGroup] = ref()
    ip_protocol = '-1'
    source_security_group_id: Ref[PrivateLoadBalancerSG] = ref()
