"""DeadLetterQueuePolicy - AWS::SQS::QueuePolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DeadLetterQueuePolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AllowEventBridgeToWriteLogs'
    principal = {
        'Service': 'events.amazonaws.com',
    }
    action = 'sqs:SendMessage'
    resource_arn = get_att(DeadLetterQueue, "Arn")
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:rule/CloudFormationEventRule'),
        },
    }


@cloudformation_dataclass
class DeadLetterQueuePolicyPolicyDocument:
    resource: PolicyDocument
    statement = [DeadLetterQueuePolicyAllowStatement0]


@cloudformation_dataclass
class DeadLetterQueuePolicy:
    """AWS::SQS::QueuePolicy resource."""

    resource: QueuePolicy
    policy_document = DeadLetterQueuePolicyPolicyDocument
    queues = [ref(DeadLetterQueue)]
