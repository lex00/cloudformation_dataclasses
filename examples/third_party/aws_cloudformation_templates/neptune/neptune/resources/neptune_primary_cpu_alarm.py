"""NeptunePrimaryCpuAlarm - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptunePrimaryCpuAlarmDimension:
    resource: Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimaryCpuAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: Alarm
    alarm_description = Sub('${Env}-${AppName} primary DB CPU over ${HighCpuAlarmThreshold}%')
    namespace = 'AWS/Neptune'
    metric_name = 'CPUUtilization'
    unit = 'Percent'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = ref(HighCpuAlarmThreshold)
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryCpuAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
    insufficient_data_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
