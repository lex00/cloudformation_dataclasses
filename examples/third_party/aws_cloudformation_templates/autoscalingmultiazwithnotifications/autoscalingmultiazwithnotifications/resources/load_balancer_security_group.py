"""LoadBalancerSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerSecurityGroupIngress:
    resource: Ingress
    ip_protocol = 'tcp'
    from_port = 443
    to_port = 443
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class LoadBalancerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Allows inbound traffic on port 443'
    security_group_ingress = [LoadBalancerSecurityGroupIngress]
    vpc_id = ref(VPC)
