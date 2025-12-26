"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


@cloudformation_dataclass
class SubscriptionEndPoint:
    """The endpoint that receives notifications from the Amazon SNS topic. The endpoint value depends on the protocol that you specify. This could be a URL or ARN"""

    resource: Parameter
    type = STRING
    description = 'The endpoint that receives notifications from the Amazon SNS topic. The endpoint value depends on the protocol that you specify. This could be a URL or ARN'


@cloudformation_dataclass
class SubscriptionProtocol:
    """The subscription's protocol"""

    resource: Parameter
    type = STRING
    description = "The subscription's protocol"
    default = 'sqs'
    allowed_values = [
    'http',
    'https',
    'email',
    'email-json',
    'sms',
    'sqs',
    'application',
    'lambda',
]
