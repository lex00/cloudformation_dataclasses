"""TargetGroup - AWS::ElasticLoadBalancingV2::TargetGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TargetGroupTargetGroupAttribute:
    resource: TargetGroupAttribute
    key = 'deregistration_delay.timeout_seconds'
    value = '10'


@cloudformation_dataclass
class TargetGroupTargetGroupAttribute1:
    resource: TargetGroupAttribute
    key = 'stickiness.enabled'
    value = 'false'


@cloudformation_dataclass
class TargetGroup:
    """AWS::ElasticLoadBalancingV2::TargetGroup resource."""

    resource: elasticloadbalancingv2.TargetGroup
    port = 80
    protocol = 'HTTP'
    target_group_attributes = [TargetGroupTargetGroupAttribute, TargetGroupTargetGroupAttribute1]
    target_type = 'ip'
    vpc_id = ref(VPCId)
