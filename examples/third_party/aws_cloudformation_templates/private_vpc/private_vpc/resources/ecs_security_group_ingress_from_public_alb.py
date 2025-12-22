from __future__ import annotations

"""EcsSecurityGroupIngressFromPublicALB - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EcsSecurityGroupIngressFromPublicALB:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    description = 'Ingress from the public ALB'
    group_id: Ref[FargateContainerSecurityGroup] = ref()
    ip_protocol = '-1'
    source_security_group_id: Ref[PublicLoadBalancerSG] = ref()
