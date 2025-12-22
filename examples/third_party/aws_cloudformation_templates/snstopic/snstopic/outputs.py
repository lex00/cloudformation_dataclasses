"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TopicARNOutput:
    """ARN of newly created SNS Topic"""

    resource: Output
    value = ref("SNSTopic")
    description = 'ARN of newly created SNS Topic'


@cloudformation_dataclass
class QueueNameOutput:
    """Name of newly created SNS Topic"""

    resource: Output
    value = get_att("SNSTopic", "TopicName")
    description = 'Name of newly created SNS Topic'
