"""ElasticLoadBalancer - AWS::ElasticLoadBalancing::LoadBalancer resource."""

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
    depends_on = ["LogsBucketPolicy"]
