from __future__ import annotations

"""ScheduledActionUp - AWS::AutoScaling::ScheduledAction resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ScheduledActionUp:
    """AWS::AutoScaling::ScheduledAction resource."""

    resource: ScheduledAction
    auto_scaling_group_name: Ref[WebServerGroup] = ref()
    max_size = '10'
    min_size = '5'
    recurrence = '0 7 * * *'
