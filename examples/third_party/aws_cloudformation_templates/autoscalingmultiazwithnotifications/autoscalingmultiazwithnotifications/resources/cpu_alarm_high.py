from __future__ import annotations

"""CPUAlarmHigh - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CPUAlarmHighDimension:
    resource: Dimension
    name = 'AutoScalingGroupName'
    value: Ref[WebServerGroup] = ref()


@cloudformation_dataclass
class CPUAlarmHigh:
    """AWS::CloudWatch::Alarm resource."""

    resource: Alarm
    alarm_description = 'Scale-up if CPU > 90% for 10 minutes'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = 90
    alarm_actions = [ref("WebServerScaleUpPolicy")]
    dimensions = [CPUAlarmHighDimension]
    comparison_operator = 'GreaterThanThreshold'
