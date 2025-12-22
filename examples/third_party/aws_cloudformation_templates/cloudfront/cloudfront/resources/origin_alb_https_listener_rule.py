from __future__ import annotations

"""OriginALBHttpsListenerRule - AWS::ElasticLoadBalancingV2::ListenerRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class OriginALBHttpsListenerRuleAction:
    resource: Action
    type_ = 'forward'
    target_group_arn: Ref[OriginALBTG] = ref()


@cloudformation_dataclass
class OriginALBHttpsListenerRuleRuleCondition:
    resource: RuleCondition
    field = 'path-pattern'
    values = ['/*']


@cloudformation_dataclass
class OriginALBHttpsListenerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: ListenerRule
    actions = [OriginALBHttpsListenerRuleAction]
    conditions = [OriginALBHttpsListenerRuleRuleCondition]
    listener_arn: Ref[OriginALBHttpsListener] = ref()
    priority = 1
    depends_on = ["OriginALBHttpsListener"]
