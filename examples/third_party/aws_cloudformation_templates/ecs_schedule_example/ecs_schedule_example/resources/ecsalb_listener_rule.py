"""ECSALBListenerRule - AWS::ElasticLoadBalancingV2::ListenerRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ECSALBListenerRuleAction:
    resource: Action
    type_ = 'forward'
    target_group_arn = ref(ECSTG)


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
    listener_arn = ref(ALBListener)
    priority = 1
    depends_on = ["ALBListener"]
