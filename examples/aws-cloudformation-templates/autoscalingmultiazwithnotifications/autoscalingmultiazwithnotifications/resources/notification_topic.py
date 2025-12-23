"""NotificationTopic - AWS::SNS::Topic resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NotificationTopicSubscription:
    resource: sns.topic.Subscription
    endpoint = ref(OperatorEMail)
    protocol = 'email'


@cloudformation_dataclass
class NotificationTopic:
    """AWS::SNS::Topic resource."""

    resource: sns.Topic
    display_name = Sub('${AWS::StackName}-NotificationTopic')
    subscription = [NotificationTopicSubscription]
    kms_master_key_id = ref(KmsKeyArn)
