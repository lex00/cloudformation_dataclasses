from __future__ import annotations

"""Channel - AWS::IoTAnalytics::Channel resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Channel:
    """AWS::IoTAnalytics::Channel resource."""

    resource: iotanalytics.Channel
    channel_name = Sub('${ProjectName}_channel')
    tags = [{
        'Key': 'Project',
        'Value': ref(ProjectName),
    }]
