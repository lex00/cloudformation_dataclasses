"""ALBListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ALBListenerAction:
    resource: elasticloadbalancingv2.listener_rule.Action
    type_ = 'forward'
    target_group_arn = ref(ECSTG)


@cloudformation_dataclass
class ALBListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [ALBListenerAction]
    load_balancer_arn = ref(ECSALB)
    port = '80'
    protocol = 'HTTP'
    depends_on = ["ECSServiceRole"]
