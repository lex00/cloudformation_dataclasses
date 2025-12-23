"""ElasticLoadBalancer - AWS::ElasticLoadBalancing::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ElasticLoadBalancerLBCookieStickinessPolicy:
    resource: elasticloadbalancing.load_balancer.LBCookieStickinessPolicy
    policy_name = 'myLBPolicy'
    cookie_expiration_period = '180'


@cloudformation_dataclass
class ElasticLoadBalancerListeners:
    resource: elasticloadbalancing.load_balancer.Listeners
    load_balancer_port = '80'
    instance_port = '80'
    protocol = 'HTTP'
    policy_names = ['myLBPolicy']


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
    instances = [ref(EC2Instance1), ref(EC2Instance2)]
    lb_cookie_stickiness_policy = [ElasticLoadBalancerLBCookieStickinessPolicy]
    listeners = [ElasticLoadBalancerListeners]
    health_check = ElasticLoadBalancerHealthCheck
