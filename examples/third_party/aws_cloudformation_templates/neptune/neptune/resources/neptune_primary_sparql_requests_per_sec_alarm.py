from __future__ import annotations

"""NeptunePrimarySparqlRequestsPerSecAlarm - AWS::CloudWatch::Alarm resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptunePrimarySparqlRequestsPerSecAlarmDimension:
    resource: Dimension
    name = 'DBClusterIdentifier'
    value = ref(NeptuneDBCluster)


@cloudformation_dataclass
class NeptunePrimarySparqlRequestsPerSecAlarm:
    """AWS::CloudWatch::Alarm resource."""

    resource: Alarm
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
