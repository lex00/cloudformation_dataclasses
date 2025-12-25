"""Messaging resources: DeadLetterQueue, CloudFormationEventRule, DeadLetterQueuePolicy."""

from . import *  # noqa: F403


@cloudformation_dataclass
class DeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    queue_name = 'CloudFormation-Logs-DLQ'


@cloudformation_dataclass
class CloudFormationEventRuleDeadLetterConfig:
    resource: events.rule.DeadLetterConfig
    arn = get_att(DeadLetterQueue, "Arn")


@cloudformation_dataclass
class CloudFormationEventRuleTarget:
    resource: events.rule.Target
    arn = ref(CentralEventBusArn)
    role_arn = get_att(EventBridgeRole, "Arn")
    id = 'CentralEventBus'
    dead_letter_config = CloudFormationEventRuleDeadLetterConfig


@cloudformation_dataclass
class CloudFormationEventRule:
    """AWS::Events::Rule resource."""

    resource: events.Rule
    name = 'CloudFormationEventRule'
    event_bus_name = Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/default')
    event_pattern = {
        'source': ['aws.cloudformation'],
    }
    state = 'ENABLED'
    targets = [CloudFormationEventRuleTarget]


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

    resource: sqs.QueuePolicy
    policy_document = DeadLetterQueuePolicyPolicyDocument
    queues = [ref(DeadLetterQueue)]
