"""SNSSubscription - AWS::SNS::Subscription resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SNSSubscription:
    """AWS::SNS::Subscription resource."""

    resource: Subscription
    endpoint = ref(SubscriptionEndPoint)
    protocol = ref(SubscriptionProtocol)
    topic_arn = ref(SNSTopic)
