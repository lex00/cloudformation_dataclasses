from __future__ import annotations

"""CPUAlarmHigh - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CPUAlarmHighDimension:
    resource: Dimension
    name = 'AutoScalingGroupName'
    value: Ref[AutoScalingGroup] = ref()


@cloudformation_dataclass
class CPUAlarmHigh:
    """AWS::CloudWatch::Alarm resource."""

    resource: Alarm
    alarm_actions = [ref("ScaleUpPolicy")]
    alarm_description = 'Scale-up if CPU > 90% for 10 minutes'
    comparison_operator = 'GreaterThanThreshold'
    dimensions = [CPUAlarmHighDimension]
    evaluation_periods = '2'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = '300'
    statistic = 'Average'
    threshold = '90'
