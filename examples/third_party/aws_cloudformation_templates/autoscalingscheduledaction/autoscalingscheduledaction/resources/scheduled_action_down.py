from __future__ import annotations

"""ScheduledActionDown - AWS::AutoScaling::ScheduledAction resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ScheduledActionDown:
    """AWS::AutoScaling::ScheduledAction resource."""

    resource: ScheduledAction
    auto_scaling_group_name: Ref[WebServerGroup] = ref()
    max_size = '1'
    min_size = '1'
    recurrence = '0 19 * * *'
