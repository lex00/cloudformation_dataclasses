from __future__ import annotations

"""CPUAlarmLow - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CPUAlarmLowDimension:
    resource: Dimension
    name = 'AutoScalingGroupName'
    value: Ref[AutoScalingGroup] = ref()


@cloudformation_dataclass
class CPUAlarmLow:
    """AWS::CloudWatch::Alarm resource."""

    resource: Alarm
    alarm_actions = [ref("ScaleDownPolicy")]
    alarm_description = 'Scale-down if CPU < 70% for 10 minutes'
    comparison_operator = 'LessThanThreshold'
    dimensions = [CPUAlarmLowDimension]
    evaluation_periods = '2'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = '300'
    statistic = 'Average'
    threshold = '70'
