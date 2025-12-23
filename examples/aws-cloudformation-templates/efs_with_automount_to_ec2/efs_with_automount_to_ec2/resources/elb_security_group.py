"""ELBSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ELBSecurityGroupEgress:
    resource: ec2.security_group.Egress
    cidr_ip = '0.0.0.0/0'
    from_port = '80'
    ip_protocol = 'tcp'
    to_port = '80'


@cloudformation_dataclass
class ELBSecurityGroupEgress1:
    resource: ec2.security_group.Egress
    cidr_ip = '0.0.0.0/0'
    from_port = '443'
    ip_protocol = 'tcp'
    to_port = '443'


@cloudformation_dataclass
class ELBSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable public access HTTP and HTTPS'
    security_group_ingress = [ELBSecurityGroupEgress, ELBSecurityGroupEgress1]
    vpc_id = ref(VPC)
