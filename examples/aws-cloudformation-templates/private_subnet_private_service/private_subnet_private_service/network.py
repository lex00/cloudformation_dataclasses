"""Network resources: TargetGroup, LoadBalancerRule."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    health_check_interval_seconds = 6
    health_check_path = '/'
    health_check_protocol = 'HTTP'
    health_check_timeout_seconds = 5
    healthy_threshold_count = 2
    target_type = 'ip'
    name = ref(ServiceName)
    port = ref(ContainerPort)
    protocol = 'HTTP'
    unhealthy_threshold_count = 2
    vpc_id = ImportValue(Join(':', [
    ref(StackName),
    'VPCId',
]))


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

    resource: elasticloadbalancingv2.ListenerRule
    actions = [LoadBalancerRuleAction]
    conditions = [LoadBalancerRuleRuleCondition]
    listener_arn = ImportValue(Join(':', [
    ref(StackName),
    'PrivateListener',
]))
    priority = ref(Priority)
