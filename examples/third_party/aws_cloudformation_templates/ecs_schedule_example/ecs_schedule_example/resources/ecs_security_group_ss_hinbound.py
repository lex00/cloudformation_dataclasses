from __future__ import annotations

"""EcsSecurityGroupSSHinbound - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EcsSecurityGroupSSHinbound:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = '192.168.1.0/0'
