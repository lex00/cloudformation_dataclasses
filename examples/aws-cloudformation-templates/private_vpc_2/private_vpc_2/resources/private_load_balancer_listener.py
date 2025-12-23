"""PrivateLoadBalancerListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateLoadBalancerListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    target_group_arn = ref(DummyTargetGroupPrivate)
    type_ = 'forward'


@cloudformation_dataclass
class PrivateLoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [PrivateLoadBalancerListenerAction]
    load_balancer_arn = ref(PrivateLoadBalancer)
    port = 80
    protocol = 'HTTP'
