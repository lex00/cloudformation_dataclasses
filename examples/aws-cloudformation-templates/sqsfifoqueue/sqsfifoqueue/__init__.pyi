"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Output,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.template import Condition as TemplateCondition
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import sqs
from cloudformation_dataclasses.intrinsics import (
    AWS_NO_VALUE,
    Equals,
    If,
    Join,
)

from .messaging import MyDeadLetterQueue as MyDeadLetterQueue
from .messaging import SQSQueue as SQSQueue
from .outputs import QueueARNOutput as QueueARNOutput
from .outputs import QueueNameOutput as QueueNameOutput
from .outputs import QueueURLOutput as QueueURLOutput
from .params import ContentBasedDeduplication as ContentBasedDeduplication
from .params import CreateDeadLetterQueueCondition as CreateDeadLetterQueueCondition
from .params import MaximumMessageSize as MaximumMessageSize
from .params import MessageRetentionPeriod as MessageRetentionPeriod
from .params import QueueName as QueueName
from .params import ReceiveMessageWaitTimeSeconds as ReceiveMessageWaitTimeSeconds
from .params import UsedeadletterQueue as UsedeadletterQueue
from .params import VisibilityTimeout as VisibilityTimeout

__all__: list[str] = ['AWS_NO_VALUE', 'ContentBasedDeduplication', 'CreateDeadLetterQueueCondition', 'Equals', 'If', 'Join', 'MaximumMessageSize', 'MessageRetentionPeriod', 'MyDeadLetterQueue', 'NUMBER', 'Output', 'Parameter', 'QueueARNOutput', 'QueueName', 'QueueNameOutput', 'QueueURLOutput', 'ReceiveMessageWaitTimeSeconds', 'SQSQueue', 'STRING', 'Template', 'TemplateCondition', 'UsedeadletterQueue', 'VisibilityTimeout', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources', 'sqs']
