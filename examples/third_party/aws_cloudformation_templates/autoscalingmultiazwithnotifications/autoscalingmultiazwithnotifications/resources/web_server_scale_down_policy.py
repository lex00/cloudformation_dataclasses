from __future__ import annotations

"""WebServerScaleDownPolicy - AWS::AutoScaling::ScalingPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerScaleDownPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    resource: ScalingPolicy
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name: Ref[WebServerGroup] = ref()
    cooldown = '60'
    scaling_adjustment = -1
