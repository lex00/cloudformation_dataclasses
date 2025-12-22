"""NeptunePrimaryMemoryAlarm - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptunePrimaryMemoryAlarmDimension:
    resource: Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimaryMemoryAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: Alarm
    alarm_description = Sub('${Env}-${AppName} primary DB memory under ${LowMemoryAlarmThreshold} bytes')
    namespace = 'AWS/Neptune'
    metric_name = 'FreeableMemory'
    unit = 'Bytes'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = ref(LowMemoryAlarmThreshold)
    comparison_operator = 'LessThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryMemoryAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
    insufficient_data_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
