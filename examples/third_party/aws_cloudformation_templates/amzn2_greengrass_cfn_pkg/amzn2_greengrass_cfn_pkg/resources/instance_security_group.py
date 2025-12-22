"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: ec2.Ingress
    cidr_ip = ref(SecurityAccessCIDR)
    from_port = 22
    ip_protocol = 'tcp'
    to_port = 22


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Allow inbound SSH access'
    security_group_ingress = [InstanceSecurityGroupIngress]
    vpc_id = ref(VPC)
