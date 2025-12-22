"""Pipeline - AWS::IoTAnalytics::Pipeline resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PipelineChannel:
    resource: iotanalytics.Channel
    name = 'ChannelActivity'
    channel_name = Sub('${ProjectName}_channel')
    next = 'DatastoreActivity'


@cloudformation_dataclass
class PipelineDatastore:
    resource: iotanalytics.Datastore
    name = 'DatastoreActivity'
    datastore_name = Sub('${ProjectName}_datastore')


@cloudformation_dataclass
class PipelineActivity:
    resource: iotanalytics.Activity
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
    depends_on = ["Channel", "Datastore"]
