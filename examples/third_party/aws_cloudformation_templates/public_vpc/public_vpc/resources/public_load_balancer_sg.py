from __future__ import annotations

"""PublicLoadBalancerSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicLoadBalancerSGIngress:
    resource: Ingress
    cidr_ip = '0.0.0.0/0'
    ip_protocol = '-1'


@cloudformation_dataclass
class PublicLoadBalancerSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: SecurityGroup
    group_description = 'Access to the public facing load balancer'
    vpc_id: Ref[VPC] = ref()
    security_group_ingress = [PublicLoadBalancerSGIngress]
