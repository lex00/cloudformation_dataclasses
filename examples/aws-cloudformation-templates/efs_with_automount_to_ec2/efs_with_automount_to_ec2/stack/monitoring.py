"""Monitoring resources: CPUAlarmHigh, CPUAlarmLow."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CPUAlarmHighDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'AutoScalingGroupName'
    value = ref(AutoScalingGroup)


@cloudformation_dataclass
class CPUAlarmHigh:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_actions = [ref(ScaleUpPolicy)]
    alarm_description = 'Scale-up if CPU > 90% for 10 minutes'
    comparison_operator = 'GreaterThanThreshold'
    dimensions = [CPUAlarmHighDimension]
    evaluation_periods = '2'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = '300'
    statistic = 'Average'
    threshold = '90'


@cloudformation_dataclass
class CPUAlarmLowDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'AutoScalingGroupName'
    value = ref(AutoScalingGroup)


@cloudformation_dataclass
class CPUAlarmLow:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_actions = [ref(ScaleDownPolicy)]
    alarm_description = 'Scale-down if CPU < 70% for 10 minutes'
    comparison_operator = 'LessThanThreshold'
    dimensions = [CPUAlarmLowDimension]
    evaluation_periods = '2'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = '300'
    statistic = 'Average'
    threshold = '70'
