from __future__ import annotations

"""EC2SecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2SecurityGroupIngress:
    resource: Ingress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class EC2SecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'SSH access'
    security_group_ingress = [EC2SecurityGroupIngress]
