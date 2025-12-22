from __future__ import annotations

"""Tcp8080Out - AWS::EC2::SecurityGroupEgress resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Tcp8080Out:
    """AWS::EC2::SecurityGroupEgress resource."""

    resource: SecurityGroupEgress
    group_id = ref(ALBExternalAccessSG)
    to_port = 8080
    ip_protocol = 'tcp'
    from_port = 8080
    destination_security_group_id = ref(EC2InstanceSG)
