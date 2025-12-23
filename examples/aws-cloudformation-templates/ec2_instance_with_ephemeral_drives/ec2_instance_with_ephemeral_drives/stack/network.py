"""Network resources: EC2SecurityGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2SecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class EC2SecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'SSH access'
    security_group_ingress = [EC2SecurityGroupEgress]
