from __future__ import annotations

"""EcsSecurityGroupIngressFromSelf - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EcsSecurityGroupIngressFromSelf:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    description = 'Ingress from other containers in the same security group'
    group_id: Ref[FargateContainerSecurityGroup] = ref()
    ip_protocol = '-1'
    source_security_group_id: Ref[FargateContainerSecurityGroup] = ref()
