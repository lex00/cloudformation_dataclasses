"""Messaging resources: MyDeadLetterQueue, SQSQueue."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyDeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    fifo_queue = 'true'
    queue_name = Join('', [
    ref(QueueName),
    'Deadletter',
    '.fifo',
])
    message_retention_period = 1209600
    condition = 'CreateDeadLetterQueue'


@cloudformation_dataclass
class SQSQueue:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
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
    'deadLetterTargetArn': get_att(MyDeadLetterQueue, "Arn"),
    'maxReceiveCount': 5,
}, AWS_NO_VALUE)
    visibility_timeout = ref(VisibilityTimeout)
