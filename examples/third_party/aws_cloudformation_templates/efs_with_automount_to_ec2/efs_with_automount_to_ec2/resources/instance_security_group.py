"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    cidr_ip = '0.0.0.0/0'
    from_port = '22'
    ip_protocol = 'tcp'
    to_port = '22'


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    from_port = '80'
    ip_protocol = 'tcp'
    source_security_group_id = get_att(ELBSecurityGroup, "GroupId")
    to_port = '80'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH public access and HTTP from the load balancer only'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupIngress]
    vpc_id = ref(VPC)
