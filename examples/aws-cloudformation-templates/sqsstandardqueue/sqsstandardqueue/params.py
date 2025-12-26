"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class DelaySeconds:
    """The time in seconds that the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes)."""

    resource: Parameter
    type = NUMBER
    description = 'The time in seconds that the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes).'
    default = '5'


@cloudformation_dataclass
class MaximumMessageSize:
    """The limit of how many bytes that a message can contain before Amazon SQS rejects it, 1024 bytes (1 KiB) to 262144 bytes (256 KiB)"""

    resource: Parameter
    type = NUMBER
    description = 'The limit of how many bytes that a message can contain before Amazon SQS rejects it, 1024 bytes (1 KiB) to 262144 bytes (256 KiB)'
    default = '262144'


@cloudformation_dataclass
class MessageRetentionPeriod:
    """The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1209600 seconds (14 days). """

    resource: Parameter
    type = NUMBER
    description = 'The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1209600 seconds (14 days). '
    default = '345600'


@cloudformation_dataclass
class ReceiveMessageWaitTimeSeconds:
    """Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, as opposed to returning an empty response if a message is not yet available. 1 to 20"""

    resource: Parameter
    type = NUMBER
    description = 'Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, as opposed to returning an empty response if a message is not yet available. 1 to 20'
    default = '0'


@cloudformation_dataclass
class UsedeadletterQueue:
    """A dead-letter queue is a queue that other (source) queues can target for messages that can't be processed (consumed) successfully. You can set aside and isolate these messages in the dead-letter queue to determine why their processing doesn't succeed."""

    resource: Parameter
    type = STRING
    description = "A dead-letter queue is a queue that other (source) queues can target for messages that can't be processed (consumed) successfully. You can set aside and isolate these messages in the dead-letter queue to determine why their processing doesn't succeed."
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


@cloudformation_dataclass
class VisibilityTimeout:
    """Time in seconds. This should be longer than the time it would take to process and delete a message, this should not exceed 12 hours."""

    resource: Parameter
    type = NUMBER
    description = 'Time in seconds. This should be longer than the time it would take to process and delete a message, this should not exceed 12 hours.'
    default = '5'


@cloudformation_dataclass
class KmsMasterKeyIdForSqs:
    """(Optional) For unencrypted leave blank. The ID or Alias of an AWS managed or a custom CMK."""

    resource: Parameter
    type = STRING
    description = '(Optional) For unencrypted leave blank. The ID or Alias of an AWS managed or a custom CMK.'
    default = 'alias/aws/sqs'


@cloudformation_dataclass
class CreateDeadLetterQueueCondition:
    resource: TemplateCondition
    logical_id = 'CreateDeadLetterQueue'
    expression = Equals(ref(UsedeadletterQueue), 'true')


@cloudformation_dataclass
class IsKmsExistCondition:
    resource: TemplateCondition
    logical_id = 'IsKmsExist'
    expression = Not(Equals('', ref(KmsMasterKeyIdForSqs)))
