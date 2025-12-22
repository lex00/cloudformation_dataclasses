"""OriginALBHttpsListenerRule - AWS::ElasticLoadBalancingV2::ListenerRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OriginALBHttpsListenerRuleAction:
    resource: elasticloadbalancingv2.Action
    type_ = 'forward'
    target_group_arn = ref(OriginALBTG)


@cloudformation_dataclass
class OriginALBHttpsListenerRuleRuleCondition:
    resource: elasticloadbalancingv2.RuleCondition
    field = 'path-pattern'
    values = ['/*']


@cloudformation_dataclass
class OriginALBHttpsListenerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: ListenerRule
    actions = [OriginALBHttpsListenerRuleAction]
    conditions = [OriginALBHttpsListenerRuleRuleCondition]
    listener_arn = ref(OriginALBHttpsListener)
    priority = 1
    depends_on = ["OriginALBHttpsListener"]
