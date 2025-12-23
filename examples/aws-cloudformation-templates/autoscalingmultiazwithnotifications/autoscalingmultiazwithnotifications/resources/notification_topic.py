"""NotificationTopic - AWS::SNS::Topic resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class NotificationTopic:
    """AWS::SNS::Topic resource."""

    # Unknown resource type: AWS::SNS::Topic
    resource: CloudFormationResource
    display_name = Sub('${AWS::StackName}-NotificationTopic')
    subscription = [{
        'Endpoint': ref(OperatorEMail),
        'Protocol': 'email',
    }]
    kms_master_key_id = ref(KmsKeyArn)
