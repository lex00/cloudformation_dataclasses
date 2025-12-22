"""ALB500sAlarmScaleUp - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ALB500sAlarmScaleUpDimension:
    resource: Dimension
    name = 'ECSService'
    value = ref(Service)


@cloudformation_dataclass
class ALB500sAlarmScaleUp:
    """AWS::CloudWatch::Alarm resource."""

    resource: Alarm
    evaluation_periods = '1'
    statistic = 'Average'
    threshold = '10'
    alarm_description = 'Alarm if our ALB generates too many HTTP 500s.'
    period = '60'
    alarm_actions = [ref(ServiceScalingPolicy)]
    namespace = 'AWS/ApplicationELB'
    dimensions = [ALB500sAlarmScaleUpDimension]
    comparison_operator = 'GreaterThanThreshold'
    metric_name = 'HTTPCode_ELB_5XX_Count'
