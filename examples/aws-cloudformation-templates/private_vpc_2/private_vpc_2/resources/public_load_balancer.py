"""PublicLoadBalancer - AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicLoadBalancerLoadBalancerAttribute:
    resource: elasticloadbalancingv2.load_balancer.LoadBalancerAttribute
    key = 'idle_timeout.timeout_seconds'
    value = '30'


@cloudformation_dataclass
class PublicLoadBalancer:
    """AWS::ElasticLoadBalancingV2::LoadBalancer resource."""

    resource: elasticloadbalancingv2.LoadBalancer
    scheme = 'internet-facing'
    load_balancer_attributes = [PublicLoadBalancerLoadBalancerAttribute]
    subnets = [ref(PublicSubnetOne), ref(PublicSubnetTwo)]
    security_groups = [ref(PublicLoadBalancerSG)]
    depends_on = ["GatewayAttachement"]
