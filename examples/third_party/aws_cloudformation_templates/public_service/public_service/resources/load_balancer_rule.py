"""LoadBalancerRule - AWS::ElasticLoadBalancingV2::ListenerRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerRuleAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    target_group_arn = ref(TargetGroup)
    type_ = 'forward'


@cloudformation_dataclass
class LoadBalancerRuleRuleCondition:
    resource: elasticloadbalancingv2.listener_rule.RuleCondition
    field = 'path-pattern'
    values = [ref(Path)]


@cloudformation_dataclass
class LoadBalancerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: ListenerRule
    actions = [LoadBalancerRuleAction]
    conditions = [LoadBalancerRuleRuleCondition]
    listener_arn = ImportValue(Join(':', [
    ref(StackName),
    'PublicListener',
]))
    priority = ref(Priority)
