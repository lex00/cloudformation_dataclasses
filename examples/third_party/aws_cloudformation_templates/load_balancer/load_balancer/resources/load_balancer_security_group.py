"""LoadBalancerSecurityGroup - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerSecurityGroupIngress:
    resource: Ingress
    cidr_ip = '0.0.0.0/0'
    description = 'Allow from anyone on port 443'
    from_port = 443
    ip_protocol = 'tcp'
    to_port = 443


@cloudformation_dataclass
class LoadBalancerSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Automatically created Security Group for ELB'
    security_group_ingress = [LoadBalancerSecurityGroupIngress]
    vpc_id = ref(VPCId)
