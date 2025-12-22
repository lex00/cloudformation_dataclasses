"""NeptunePrimaryGremlinRequestsPerSecAlarm - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptunePrimaryGremlinRequestsPerSecAlarmDimension:
    resource: cloudwatch.Dimension
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
