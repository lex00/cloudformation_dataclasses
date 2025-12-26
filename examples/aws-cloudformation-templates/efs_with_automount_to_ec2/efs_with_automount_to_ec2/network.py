"""Network resources: ELBSecurityGroup, InstanceSecurityGroup, EFSSecurityGroup, ElasticLoadBalancer."""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import IpProtocol


@cloudformation_dataclass
class ELBSecurityGroupEgress:
    resource: ec2.security_group.Egress
    cidr_ip = '0.0.0.0/0'
    from_port = '80'
    ip_protocol = IpProtocol.TCP
    to_port = '80'


@cloudformation_dataclass
class ELBSecurityGroupEgress1:
    resource: ec2.security_group.Egress
    cidr_ip = '0.0.0.0/0'
    from_port = '443'
    ip_protocol = IpProtocol.TCP
    to_port = '443'


@cloudformation_dataclass
class ELBSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable public access HTTP and HTTPS'
    security_group_ingress = [ELBSecurityGroupEgress, ELBSecurityGroupEgress1]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    cidr_ip = '0.0.0.0/0'
    from_port = '22'
    ip_protocol = IpProtocol.TCP
    to_port = '22'


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    from_port = '80'
    ip_protocol = IpProtocol.TCP
    source_security_group_id = get_att(ELBSecurityGroup, "GroupId")
    to_port = '80'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH public access and HTTP from the load balancer only'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupIngress]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class EFSSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    from_port = '2049'
    ip_protocol = IpProtocol.TCP
    to_port = '2049'
    source_security_group_id = get_att(InstanceSecurityGroup, "GroupId")


@cloudformation_dataclass
class EFSSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable NFS access from EC2'
    security_group_ingress = [EFSSecurityGroupIngress]
    vpc_id = ref(VPC)


@cloudformation_dataclass
class ElasticLoadBalancerHealthCheck:
    resource: elasticloadbalancing.load_balancer.HealthCheck
    healthy_threshold = '3'
    interval = '30'
    target = Join('', [
    'HTTP:',
    '80',
    '/',
])
    timeout = '5'
    unhealthy_threshold = '5'


@cloudformation_dataclass
class ElasticLoadBalancerListeners:
    resource: elasticloadbalancing.load_balancer.Listeners
    instance_port = '80'
    load_balancer_port = '80'
    protocol = 'HTTP'


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    resource: elasticloadbalancing.LoadBalancer
    security_groups = [ref(ELBSecurityGroup)]
    subnets = ref(Subnets)
    cross_zone = 'true'
    health_check = ElasticLoadBalancerHealthCheck
    listeners = [ElasticLoadBalancerListeners]
