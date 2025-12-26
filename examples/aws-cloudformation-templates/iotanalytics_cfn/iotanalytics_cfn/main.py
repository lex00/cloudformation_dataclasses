"""Stack resources."""

from . import *  # noqa: F403


@cloudformation_dataclass
class Channel:
    """AWS::IoTAnalytics::Channel resource."""

    resource: iotanalytics.Channel
    channel_name = Sub('${ProjectName}_channel')
    tags = [{
        'Key': 'Project',
        'Value': ref(ProjectName),
    }]


@cloudformation_dataclass
class Datastore:
    """AWS::IoTAnalytics::Datastore resource."""

    resource: iotanalytics.Datastore
    datastore_name = Sub('${ProjectName}_datastore')
    tags = [{
        'Key': 'Project',
        'Value': ref(ProjectName),
    }]


@cloudformation_dataclass
class PipelineChannel:
    resource: iotanalytics.pipeline.Channel
    name = 'ChannelActivity'
    channel_name = Sub('${ProjectName}_channel')
    next = 'DatastoreActivity'


@cloudformation_dataclass
class PipelineDatastore:
    resource: iotanalytics.pipeline.Datastore
    name = 'DatastoreActivity'
    datastore_name = Sub('${ProjectName}_datastore')


@cloudformation_dataclass
class PipelineActivity:
    resource: iotanalytics.pipeline.Activity
    channel = PipelineChannel
    datastore = PipelineDatastore


@cloudformation_dataclass
class Pipeline:
    """AWS::IoTAnalytics::Pipeline resource."""

    resource: iotanalytics.Pipeline
    pipeline_name = Sub('${ProjectName}_pipeline')
    pipeline_activities = [PipelineActivity]
    tags = [{
        'Key': 'Project',
        'Value': ref(ProjectName),
    }]
    depends_on = [Channel, Datastore]


@cloudformation_dataclass
class SqlDatasetQueryAction:
    resource: iotanalytics.dataset.QueryAction
    sql_query = ref(SqlQuery)


@cloudformation_dataclass
class SqlDatasetAction:
    resource: iotanalytics.dataset.Action
    action_name = 'SqlAction'
    query_action = SqlDatasetQueryAction


@cloudformation_dataclass
class SqlDatasetSchedule:
    resource: iotanalytics.dataset.Schedule
    schedule_expression = ref(ScheduleExpression)


@cloudformation_dataclass
class SqlDatasetTrigger:
    resource: iotanalytics.dataset.Trigger
    schedule = SqlDatasetSchedule


@cloudformation_dataclass
class SqlDatasetRetentionPeriod:
    resource: iotanalytics.channel.RetentionPeriod
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
    depends_on = [Datastore]
