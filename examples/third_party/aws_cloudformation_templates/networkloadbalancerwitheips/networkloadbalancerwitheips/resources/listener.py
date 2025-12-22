from __future__ import annotations

"""Listener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ListenerAction:
    resource: Action
    type_ = 'forward'
    target_group_arn: Ref[TargetGroup] = ref()


@cloudformation_dataclass
class Listener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: elasticloadbalancingv2.Listener
    default_actions = [ListenerAction]
    load_balancer_arn: Ref[loadBalancer] = ref()
    port = '80'
    protocol = 'TCP'
