"""ScheduledActionUp - AWS::AutoScaling::ScheduledAction resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ScheduledActionUp:
    """AWS::AutoScaling::ScheduledAction resource."""

    # Unknown resource type: AWS::AutoScaling::ScheduledAction
    resource: CloudFormationResource
    auto_scaling_group_name = ref(WebServerGroup)
    max_size = '10'
    min_size = '5'
    recurrence = '0 7 * * *'
