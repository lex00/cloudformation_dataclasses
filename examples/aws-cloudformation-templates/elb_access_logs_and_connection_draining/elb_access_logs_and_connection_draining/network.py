"""Network resources: ElasticLoadBalancer, InstanceSecurityGroup."""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import IpProtocol


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
class ElasticLoadBalancerConnectionDrainingPolicy:
    resource: elasticloadbalancing.load_balancer.ConnectionDrainingPolicy
    enabled = 'true'
    timeout = '300'


@cloudformation_dataclass
class ElasticLoadBalancerAccessLoggingPolicy:
    resource: elasticloadbalancing.load_balancer.AccessLoggingPolicy
    s3_bucket_name = ref(LogsBucket)
    s3_bucket_prefix = 'Logs'
    enabled = 'true'
    emit_interval = '60'


@cloudformation_dataclass
class ElasticLoadBalancer:
    """AWS::ElasticLoadBalancing::LoadBalancer resource."""

    resource: elasticloadbalancing.LoadBalancer
    availability_zones = GetAZs()
    cross_zone = 'true'
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck
    connection_draining_policy = ElasticLoadBalancerConnectionDrainingPolicy
    access_logging_policy = ElasticLoadBalancerAccessLoggingPolicy
    depends_on = [LogsBucketPolicy]


@cloudformation_dataclass
class InstanceSecurityGroupEgress:
    resource: ec2.security_group.Egress
    ip_protocol = IpProtocol.TCP
    from_port = '22'
    to_port = '22'
    cidr_ip = ref(SSHLocation)


@cloudformation_dataclass
class InstanceSecurityGroupEgress1:
    resource: ec2.security_group.Egress
    ip_protocol = IpProtocol.TCP
    from_port = '80'
    to_port = '80'
    cidr_ip = '0.0.0.0/0'


@cloudformation_dataclass
class InstanceSecurityGroup:
    """AWS::EC2::SecurityGroup resource."""

    resource: ec2.SecurityGroup
    group_description = 'Enable SSH access and HTTP access on the configured port'
    security_group_ingress = [InstanceSecurityGroupEgress, InstanceSecurityGroupEgress1]
