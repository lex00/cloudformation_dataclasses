"""Network resources: KWOSSecurityGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KWOSSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class KWOSSecurityGroupEgress1:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '8888'
    to_port = '8888'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class KWOSSecurityGroupEgress2:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '443'
    to_port = '443'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class KWOSSecurityGroupEgress3:
    resource: ec2.security_group.Egress
    ip_protocol = 'icmp'
    from_port = '-1'
    to_port = '-1'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class KWOSSecurityGroupEgress4:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class KWOSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    vpc_id = ref(VpcId)
    group_description = 'Enable HTTP access via port 80/22/443 and ICMP access via port *'
    security_group_ingress = [KWOSSecurityGroupEgress, KWOSSecurityGroupEgress1, KWOSSecurityGroupEgress2, KWOSSecurityGroupEgress3, KWOSSecurityGroupEgress4]
