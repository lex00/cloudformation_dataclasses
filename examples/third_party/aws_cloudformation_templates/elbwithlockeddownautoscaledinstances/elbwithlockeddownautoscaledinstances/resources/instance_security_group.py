from __future__ import annotations

"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: Ingress
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    source_security_group_owner_id: GetAtt[ElasticLoadBalancer] = get_att("SourceSecurityGroup.OwnerAlias")
    source_security_group_name: GetAtt[ElasticLoadBalancer] = get_att("SourceSecurityGroup.GroupName")


@cloudformation_dataclass
class InstanceSecurityGroupIngress1:
    resource: Ingress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Enable SSH access and HTTP access on the inbound port'
    security_group_ingress = [InstanceSecurityGroupIngress, InstanceSecurityGroupIngress1]
