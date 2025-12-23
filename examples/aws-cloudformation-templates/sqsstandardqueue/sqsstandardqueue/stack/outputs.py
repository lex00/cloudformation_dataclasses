"""Template outputs."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class QueueURLOutput:
    """URL of newly created SQS Queue"""

    resource: Output
    value = ref(SQSQueue)
    description = 'URL of newly created SQS Queue'


@cloudformation_dataclass
class QueueARNOutput:
    """ARN of newly created SQS Queue"""

    resource: Output
    value = get_att(SQSQueue, "Arn")
    description = 'ARN of newly created SQS Queue'


@cloudformation_dataclass
class QueueNameOutput:
    """Name newly created SQS Queue"""

    resource: Output
    value = get_att(SQSQueue, "QueueName")
    description = 'Name newly created SQS Queue'


@cloudformation_dataclass
class DeadLetterQueueURLOutput:
    """URL of the dead letter queue"""

    resource: Output
    value = ref(MyDeadLetterQueue)
    description = 'URL of the dead letter queue'
    condition = 'CreateDeadLetterQueue'


@cloudformation_dataclass
class DeadLetterQueueARNOutput:
    """ARN of the dead letter queue"""

    resource: Output
    value = get_att(MyDeadLetterQueue, "Arn")
    description = 'ARN of the dead letter queue'
    condition = 'CreateDeadLetterQueue'
