"""DirectoryMonitoringTopic - AWS::SNS::Topic resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectoryMonitoringTopicSubscription:
    resource: Subscription
    endpoint = ref(DirectoryMonitoringEmail)
    protocol = 'email'


@cloudformation_dataclass
class DirectoryMonitoringTopic:
    """AWS::SNS::Topic resource."""

    resource: Topic
    kms_master_key_id = If("DirectoryMonitoringSNSTopicKMSKeyCondition", ref(DirectoryMonitoringSNSTopicKMSKey), 'aws/sns')
    subscription = [DirectoryMonitoringTopicSubscription]
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }, {
        'Key': 'DirectoryID',
        'Value': ref(DirectoryID),
    }]
