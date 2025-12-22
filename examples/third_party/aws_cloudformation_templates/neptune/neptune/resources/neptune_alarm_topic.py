from __future__ import annotations

"""NeptuneAlarmTopic - AWS::SNS::Topic resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneAlarmTopic:
    """AWS::SNS::Topic resource."""

    resource: Topic
    display_name = Sub('${AWS::StackName} alarm topic')
    condition = 'CreateSnsTopic'
