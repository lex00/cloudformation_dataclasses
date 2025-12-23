"""NeptuneAlarmSubscription - AWS::SNS::Subscription resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneAlarmSubscription:
    """AWS::SNS::Subscription resource."""

    resource: sns.Subscription
    endpoint = ref(SNSEmailSubscription)
    protocol = 'email'
    topic_arn = If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))
    condition = 'CreateSnsSubscription'
