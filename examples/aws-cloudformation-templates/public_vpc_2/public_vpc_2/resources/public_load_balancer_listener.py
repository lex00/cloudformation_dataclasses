"""PublicLoadBalancerListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicLoadBalancerListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    target_group_arn = ref(DummyTargetGroupPublic)
    type_ = 'forward'


@cloudformation_dataclass
class PublicLoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [PublicLoadBalancerListenerAction]
    load_balancer_arn = ref(PublicLoadBalancer)
    port = 80
    protocol = 'HTTP'
