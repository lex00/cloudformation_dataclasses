"""Monitoring resources: NeptunePrimaryCpuAlarm, NeptunePrimaryMemoryAlarm, NeptunePrimaryGremlinRequestsPerSecAlarm, NeptunePrimarySparqlRequestsPerSecAlarm."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptunePrimaryCpuAlarmDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimaryCpuAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
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


@cloudformation_dataclass
class NeptunePrimaryMemoryAlarmDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimaryMemoryAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
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


@cloudformation_dataclass
class NeptunePrimaryGremlinRequestsPerSecAlarmDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'DBClusterIdentifier'
    value = 'gremlin-cluster'


@cloudformation_dataclass
class NeptunePrimaryGremlinRequestsPerSecAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = Sub('${Env}-${AppName} primary DB Gremlin Requests Per Second')
    namespace = 'AWS/Neptune'
    metric_name = 'GremlinRequestsPerSec'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = ref(GremlinRequestsPerSecThreshold)
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimaryGremlinRequestsPerSecAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
    insufficient_data_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]


@cloudformation_dataclass
class NeptunePrimarySparqlRequestsPerSecAlarmDimension:
    resource: cloudwatch.anomaly_detector.Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimarySparqlRequestsPerSecAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: cloudwatch.Alarm
    alarm_description = Sub('${Env}-${AppName} primary DB Sparql Requests Per Second')
    namespace = 'AWS/Neptune'
    metric_name = 'SparqlRequestsPerSec'
    statistic = 'Average'
    period = 300
    evaluation_periods = 2
    threshold = ref(SparqlRequestsPerSecThreshold)
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    dimensions = [NeptunePrimarySparqlRequestsPerSecAlarmDimension]
    alarm_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
    insufficient_data_actions = [If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))]
