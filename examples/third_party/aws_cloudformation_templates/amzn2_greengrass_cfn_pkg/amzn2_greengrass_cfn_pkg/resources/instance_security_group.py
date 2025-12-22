from __future__ import annotations

"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: Ingress
    cidr_ip = ref(SecurityAccessCIDR)
    from_port = 22
    ip_protocol = 'tcp'
    to_port = 22


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Allow inbound SSH access'
    security_group_ingress = [InstanceSecurityGroupIngress]
    vpc_id: Ref[VPC] = ref()
