"""Messaging resources: NeptuneAlarmTopic, NeptuneAlarmSubscription."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NeptuneAlarmTopic:
    """AWS::SNS::Topic resource."""

    resource: sns.Topic
    display_name = Sub('${AWS::StackName} alarm topic')
    condition = 'CreateSnsTopic'


@cloudformation_dataclass
class NeptuneAlarmSubscription:
    """AWS::SNS::Subscription resource."""

    resource: sns.Subscription
    endpoint = ref(SNSEmailSubscription)
    protocol = 'email'
    topic_arn = If("CreateSnsTopic", ref(NeptuneAlarmTopic), ref(NeptuneSNSTopicArn))
    condition = 'CreateSnsSubscription'
