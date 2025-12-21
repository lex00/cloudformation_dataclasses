from __future__ import annotations

"""PrivateLoadBalancerListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateLoadBalancerListenerAction:
    resource: Action
    target_group_arn: Ref[DummyTargetGroupPrivate] = ref()
    type_ = 'forward'


@cloudformation_dataclass
class PrivateLoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: Listener
    default_actions = [PrivateLoadBalancerListenerAction]
    load_balancer_arn: Ref[PrivateLoadBalancer] = ref()
    port = 80
    protocol = 'HTTP'
