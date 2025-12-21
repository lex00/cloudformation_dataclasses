from __future__ import annotations

"""PublicLoadBalancerListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PublicLoadBalancerListenerAction:
    resource: Action
    target_group_arn: Ref[DummyTargetGroupPublic] = ref()
    type_ = 'forward'


@cloudformation_dataclass
class PublicLoadBalancerListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: Listener
    default_actions = [PublicLoadBalancerListenerAction]
    load_balancer_arn: Ref[PublicLoadBalancer] = ref()
    port = 80
    protocol = 'HTTP'
