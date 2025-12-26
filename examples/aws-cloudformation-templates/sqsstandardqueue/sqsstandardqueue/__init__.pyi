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
    Not,
)

from .messaging import MyDeadLetterQueue as MyDeadLetterQueue
from .messaging import SQSQueue as SQSQueue
from .outputs import DeadLetterQueueARNOutput as DeadLetterQueueARNOutput
from .outputs import DeadLetterQueueURLOutput as DeadLetterQueueURLOutput
from .outputs import QueueARNOutput as QueueARNOutput
from .outputs import QueueNameOutput as QueueNameOutput
from .outputs import QueueURLOutput as QueueURLOutput
from .params import CreateDeadLetterQueueCondition as CreateDeadLetterQueueCondition
from .params import DelaySeconds as DelaySeconds
from .params import IsKmsExistCondition as IsKmsExistCondition
from .params import KmsMasterKeyIdForSqs as KmsMasterKeyIdForSqs
from .params import MaximumMessageSize as MaximumMessageSize
from .params import MessageRetentionPeriod as MessageRetentionPeriod
from .params import ReceiveMessageWaitTimeSeconds as ReceiveMessageWaitTimeSeconds
from .params import UsedeadletterQueue as UsedeadletterQueue
from .params import VisibilityTimeout as VisibilityTimeout

__all__: list[str] = ['AWS_NO_VALUE', 'CreateDeadLetterQueueCondition', 'DeadLetterQueueARNOutput', 'DeadLetterQueueURLOutput', 'DelaySeconds', 'Equals', 'If', 'IsKmsExistCondition', 'KmsMasterKeyIdForSqs', 'MaximumMessageSize', 'MessageRetentionPeriod', 'MyDeadLetterQueue', 'NUMBER', 'Not', 'Output', 'Parameter', 'QueueARNOutput', 'QueueNameOutput', 'QueueURLOutput', 'ReceiveMessageWaitTimeSeconds', 'SQSQueue', 'STRING', 'Template', 'TemplateCondition', 'UsedeadletterQueue', 'VisibilityTimeout', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources', 'sqs']
