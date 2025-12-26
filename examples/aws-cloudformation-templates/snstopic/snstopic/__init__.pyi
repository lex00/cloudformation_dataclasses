"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import sns

from .messaging import SNSSubscription as SNSSubscription
from .messaging import SNSTopic as SNSTopic
from .outputs import QueueNameOutput as QueueNameOutput
from .outputs import TopicARNOutput as TopicARNOutput
from .params import SubscriptionEndPoint as SubscriptionEndPoint
from .params import SubscriptionProtocol as SubscriptionProtocol

__all__: list[str] = ['Output', 'Parameter', 'QueueNameOutput', 'SNSSubscription', 'SNSTopic', 'STRING', 'SubscriptionEndPoint', 'SubscriptionProtocol', 'Template', 'TopicARNOutput', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources', 'sns']
