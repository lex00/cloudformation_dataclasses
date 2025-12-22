"""CPUAlarmLow - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CPUAlarmLowDimension:
    resource: cloudwatch.Dimension
    name = 'AutoScalingGroupName'
    value = ref(WebServerGroup)


@cloudformation_dataclass
class CPUAlarmLow:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = 'Scale-down if CPU < 70% for 10 minutes'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = 70
    alarm_actions = [ref(WebServerScaleDownPolicy)]
    dimensions = [CPUAlarmLowDimension]
    comparison_operator = 'LessThanThreshold'
