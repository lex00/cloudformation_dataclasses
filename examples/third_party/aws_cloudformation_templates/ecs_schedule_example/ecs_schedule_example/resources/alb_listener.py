from __future__ import annotations

"""ALBListener - AWS::ElasticLoadBalancingV2::Listener resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ALBListenerAction:
    resource: Action
    type_ = 'forward'
    target_group_arn: Ref[ECSTG] = ref()


@cloudformation_dataclass
class ALBListener:
    """AWS::ElasticLoadBalancingV2::Listener resource."""

    resource: Listener
    default_actions = [ALBListenerAction]
    load_balancer_arn: Ref[ECSALB] = ref()
    port = '80'
    protocol = 'HTTP'
    depends_on = ["ECSServiceRole"]
