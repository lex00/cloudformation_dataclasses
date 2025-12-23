"""Datastore - AWS::IoTAnalytics::Datastore resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Datastore:
    """AWS::IoTAnalytics::Datastore resource."""

    resource: iotanalytics.Datastore
    datastore_name = Sub('${ProjectName}_datastore')
    tags = [{
        'Key': 'Project',
        'Value': ref(ProjectName),
    }]
