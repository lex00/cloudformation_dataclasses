"""MyDeadLetterQueue - AWS::SQS::Queue resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyDeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: Queue
    fifo_queue = 'true'
    queue_name = Join('', [
    ref(QueueName),
    'Deadletter',
    '.fifo',
])
    message_retention_period = 1209600
    condition = 'CreateDeadLetterQueue'
