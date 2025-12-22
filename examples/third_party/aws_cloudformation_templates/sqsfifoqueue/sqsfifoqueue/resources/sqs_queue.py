from __future__ import annotations

"""SQSQueue - AWS::SQS::Queue resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SQSQueue:
    """AWS::SQS::Queue resource."""

    resource: Queue
    content_based_deduplication = ref(ContentBasedDeduplication)
    fifo_queue = 'true'
    queue_name = Join('', [
    ref(QueueName),
    '.fifo',
])
    maximum_message_size = ref(MaximumMessageSize)
    message_retention_period = ref(MessageRetentionPeriod)
    receive_message_wait_time_seconds = ref(ReceiveMessageWaitTimeSeconds)
    redrive_policy = If("CreateDeadLetterQueue", {
    'deadLetterTargetArn': get_att("MyDeadLetterQueue", "Arn"),
    'maxReceiveCount': 5,
}, AWS_NO_VALUE)
    visibility_timeout = ref(VisibilityTimeout)
