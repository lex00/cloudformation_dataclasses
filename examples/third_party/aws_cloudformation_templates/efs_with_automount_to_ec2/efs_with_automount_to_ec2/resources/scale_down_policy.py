from __future__ import annotations

"""ScaleDownPolicy - AWS::AutoScaling::ScalingPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ScaleDownPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    resource: ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(AutoScalingGroup)
    cooldown = '60'
    scaling_adjustment = '-1'
