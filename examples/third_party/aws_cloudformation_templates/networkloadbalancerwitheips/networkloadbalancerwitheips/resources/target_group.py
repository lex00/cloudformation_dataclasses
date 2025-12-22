from __future__ import annotations

"""TargetGroup - AWS::ElasticLoadBalancingV2::TargetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TargetGroupTargetGroupAttribute:
    resource: TargetGroupAttribute
    key = 'deregistration_delay.timeout_seconds'
    value = '20'


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    name = 'MyTargets'
    port = 10
    protocol = 'TCP'
    target_group_attributes = [TargetGroupTargetGroupAttribute]
    vpc_id = Select(0, ref(VPC))
