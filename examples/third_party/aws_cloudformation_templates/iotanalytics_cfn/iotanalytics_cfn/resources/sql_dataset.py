"""SqlDataset - AWS::IoTAnalytics::Dataset resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SqlDatasetQueryAction:
    resource: QueryAction
    sql_query = ref(SqlQuery)


@cloudformation_dataclass
class SqlDatasetAction:
    resource: iotanalytics.Action
    action_name = 'SqlAction'
    query_action = SqlDatasetQueryAction


@cloudformation_dataclass
class SqlDatasetSchedule:
    resource: iotanalytics.Schedule
    schedule_expression = ref(ScheduleExpression)


@cloudformation_dataclass
class SqlDatasetTrigger:
    resource: iotanalytics.Trigger
    schedule = SqlDatasetSchedule


@cloudformation_dataclass
class SqlDatasetRetentionPeriod:
    resource: iotanalytics.RetentionPeriod
    unlimited = False
    number_of_days = 30


@cloudformation_dataclass
class SqlDataset:
    """AWS::IoTAnalytics::Dataset resource."""

    resource: iotanalytics.Dataset
    dataset_name = Sub('${ProjectName}_dataset')
    actions = [SqlDatasetAction]
    triggers = [SqlDatasetTrigger]
    retention_period = SqlDatasetRetentionPeriod
    tags = [{
        'Key': 'Project',
        'Value': ref(ProjectName),
    }]
    depends_on = ["Datastore"]
