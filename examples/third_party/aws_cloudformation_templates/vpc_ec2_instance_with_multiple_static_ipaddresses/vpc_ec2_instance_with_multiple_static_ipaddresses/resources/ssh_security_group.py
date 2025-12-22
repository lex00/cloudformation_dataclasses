"""SSHSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SSHSecurityGroupIngress:
    resource: ec2.Ingress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class SSHSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    vpc_id = ref(VpcId)
    group_description = 'Enable SSH access via port 22'
    security_group_ingress = [SSHSecurityGroupIngress]
