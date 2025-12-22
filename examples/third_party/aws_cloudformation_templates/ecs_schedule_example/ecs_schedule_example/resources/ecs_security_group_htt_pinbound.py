from __future__ import annotations

"""EcsSecurityGroupHTTPinbound - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EcsSecurityGroupHTTPinbound:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    group_id = ref(EcsSecurityGroup)
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'
