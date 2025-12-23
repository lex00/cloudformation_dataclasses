"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class SNSTopic:
    """AWS::SNS::Topic resource."""

    resource: sns.Topic


@cloudformation_dataclass
class SNSSubscription:
    """AWS::SNS::Subscription resource."""

    resource: sns.Subscription
    endpoint = ref(SubscriptionEndPoint)
    protocol = ref(SubscriptionProtocol)
    topic_arn = ref(SNSTopic)
