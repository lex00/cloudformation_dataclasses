"""Network resources: ElasticLoadBalancer, InstanceSecurityGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ElasticLoadBalancerListeners:
    resource: elasticloadbalancing.load_balancer.Listeners
    load_balancer_port = '80'
    instance_port = '80'
    protocol = 'HTTP'


@cloudformation_dataclass
class ElasticLoadBalancerHealthCheck:
    resource: elasticloadbalancing.load_balancer.HealthCheck
    target = 'HTTP:80/'
    healthy_threshold = '3'
    unhealthy_threshold = '5'
    interval = '30'
    timeout = '5'


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    resource: elasticloadbalancing.LoadBalancer
    availability_zones = GetAZs()
    cross_zone = 'true'
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck


@cloudformation_dataclass
class InstanceSecurityGroupIngress:
    resource: ec2.security_group.Ingress
    ip_protocol = 'tcp'
    from_port = '80'
    to_port = '80'
    source_security_group_owner_id = get_att(ElasticLoadBalancer, "SourceSecurityGroup.OwnerAlias")
    source_security_group_name = get_att(ElasticLoadBalancer, "SourceSecurityGroup.GroupName")


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = 'tcp'
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP access on the inbound port'
    security_group_ingress = [InstanceSecurityGroupIngress, InstanceSecurityGroupEgress]
