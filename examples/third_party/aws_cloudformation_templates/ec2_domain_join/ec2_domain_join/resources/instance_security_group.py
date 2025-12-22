"""InstanceSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: Ingress
    ip_protocol = 'tcp'
    from_port = '3389'
    to_port = '3389'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Allow http to client host'
    vpc_id = ref(VPC)
    security_group_ingress = [InstanceSecurityGroupIngress]
