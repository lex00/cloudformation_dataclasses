from __future__ import annotations

"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: Ingress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Enable SSH access via port 22'
    security_group_ingress = [InstanceSecurityGroupIngress]
