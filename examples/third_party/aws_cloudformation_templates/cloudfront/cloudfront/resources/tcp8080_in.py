from __future__ import annotations

"""Tcp8080In - AWS::EC2::SecurityGroupIngress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Tcp8080In:
    """AWS::EC2::SecurityGroupIngress resource."""

    resource: SecurityGroupIngress
    group_id: Ref[EC2InstanceSG] = ref()
    to_port = '8080'
    ip_protocol = 'tcp'
    from_port = '8080'
    source_security_group_id: Ref[ALBExternalAccessSG] = ref()
