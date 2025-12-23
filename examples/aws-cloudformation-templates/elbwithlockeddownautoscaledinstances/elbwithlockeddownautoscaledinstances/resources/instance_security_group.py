"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    source_security_group_owner_id = get_att(ElasticLoadBalancer, "SourceSecurityGroup.OwnerAlias")
    source_security_group_name = get_att(ElasticLoadBalancer, "SourceSecurityGroup.GroupName")


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP access on the inbound port'
    security_group_ingress = [InstanceSecurityGroupIngress, InstanceSecurityGroupEgress]
