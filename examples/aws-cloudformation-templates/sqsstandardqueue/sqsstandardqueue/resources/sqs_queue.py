"""SQSQueue - AWS::SQS::Queue resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SQSQueue:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    delay_seconds = ref(DelaySeconds)
    maximum_message_size = ref(MaximumMessageSize)
    message_retention_period = ref(MessageRetentionPeriod)
    receive_message_wait_time_seconds = ref(ReceiveMessageWaitTimeSeconds)
    kms_master_key_id = If("IsKmsExist", ref(KmsMasterKeyIdForSqs), AWS_NO_VALUE)
    redrive_policy = If("CreateDeadLetterQueue", {
    'deadLetterTargetArn': get_att(MyDeadLetterQueue, "Arn"),
    'maxReceiveCount': 5,
}, AWS_NO_VALUE)
    visibility_timeout = ref(VisibilityTimeout)
