from __future__ import annotations

"""LoadBalancerRule - AWS::ElasticLoadBalancingV2::ListenerRule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LoadBalancerRuleAction:
    resource: Action
    target_group_arn: Ref[TargetGroup] = ref()
    type_ = 'forward'


@cloudformation_dataclass
class LoadBalancerRuleRuleCondition:
    resource: RuleCondition
    field = 'path-pattern'
    values = [ref(Path)]


@cloudformation_dataclass
class LoadBalancerRule:
    """AWS::ElasticLoadBalancingV2::ListenerRule resource."""

    resource: ListenerRule
    actions = [LoadBalancerRuleAction]
    conditions = [LoadBalancerRuleRuleCondition]
    listener_arn = ImportValue({
    'Fn::Join': [
        ':',
        [
            ref(StackName),
            'PublicListener',
        ],
    ],
})
    priority = ref(Priority)
