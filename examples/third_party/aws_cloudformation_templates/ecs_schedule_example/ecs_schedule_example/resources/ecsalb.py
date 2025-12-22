"""ECSALB - AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSALBLoadBalancerAttribute:
    resource: LoadBalancerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


@cloudformation_dataclass
class ECSALB:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    name = 'ECSALB'
    scheme = 'internet-facing'
    load_balancer_attributes = [ECSALBLoadBalancerAttribute]
    subnets = ref(SubnetId)
    security_groups = [ref(EcsSecurityGroup)]
