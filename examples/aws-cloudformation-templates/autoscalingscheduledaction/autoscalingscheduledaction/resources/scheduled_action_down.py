"""ScheduledActionDown - AWS::AutoScaling::ScheduledAction resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ScheduledActionDown:
    """AWS::AutoScaling::ScheduledAction resource."""

    resource: autoscaling.ScheduledAction
    auto_scaling_group_name = ref(WebServerGroup)
    max_size = '1'
    min_size = '1'
    recurrence = '0 19 * * *'
