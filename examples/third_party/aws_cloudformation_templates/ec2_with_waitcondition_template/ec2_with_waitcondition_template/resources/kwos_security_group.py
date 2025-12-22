"""KWOSSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KWOSSecurityGroupIngress:
    resource: ec2.Ingress
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class KWOSSecurityGroupIngress1:
    resource: ec2.Ingress
    ip_protocol = 'tcp'
    from_port = '8888'
    to_port = '8888'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class KWOSSecurityGroupIngress2:
    resource: ec2.Ingress
    ip_protocol = 'tcp'
    from_port = '443'
    to_port = '443'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class KWOSSecurityGroupIngress3:
    resource: ec2.Ingress
    ip_protocol = 'icmp'
    from_port = '-1'
    to_port = '-1'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class KWOSSecurityGroupIngress4:
    resource: ec2.Ingress
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
    security_group_ingress = [KWOSSecurityGroupIngress, KWOSSecurityGroupIngress1, KWOSSecurityGroupIngress2, KWOSSecurityGroupIngress3, KWOSSecurityGroupIngress4]
