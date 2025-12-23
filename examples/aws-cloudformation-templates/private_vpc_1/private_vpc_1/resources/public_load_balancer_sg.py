"""PublicLoadBalancerSG - AWS::EC2::SecurityGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicLoadBalancerSG:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Access to the public facing load balancer'
    vpc_id = ref(VPC)
    security_group_ingress = [{
        'CidrIp': '0.0.0.0/0',
        'IpProtocol': -1,
    }]
