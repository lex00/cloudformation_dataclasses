from __future__ import annotations

"""ECSALBListenerRule - AWS::ElasticLoadBalancingV2::ListenerRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSALBListenerRuleAction:
    resource: Action
    type_ = 'forward'
    target_group_arn: Ref[ECSTG] = ref()


@cloudformation_dataclass
class ECSALBListenerRuleRuleCondition:
    resource: RuleCondition
    field = 'path-pattern'
    values = ['/']


@cloudformation_dataclass
class ECSALBListenerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: ListenerRule
    actions = [ECSALBListenerRuleAction]
    conditions = [ECSALBListenerRuleRuleCondition]
    listener_arn: Ref[ALBListener] = ref()
    priority = 1
    depends_on = ["ALBListener"]
