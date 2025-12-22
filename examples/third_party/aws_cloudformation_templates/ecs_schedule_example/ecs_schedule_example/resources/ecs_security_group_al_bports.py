from __future__ import annotations

"""EcsSecurityGroupALBports - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EcsSecurityGroupALBports:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = 'tcp'
    from_port = '31000'
    to_port = '61000'
    source_security_group_id = ref(EcsSecurityGroup)
