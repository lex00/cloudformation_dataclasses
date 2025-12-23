"""WebServerScaleDownPolicy - AWS::AutoScaling::ScalingPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerScaleDownPolicy:
    """AWS::AutoScaling::ScalingPolicy resource."""

    # Unknown resource type: AWS::AutoScaling::ScalingPolicy
    resource: CloudFormationResource
    adjustment_type = 'ChangeInCapacity'
    auto_scaling_group_name = ref(WebServerGroup)
    cooldown = '60'
    scaling_adjustment = -1
