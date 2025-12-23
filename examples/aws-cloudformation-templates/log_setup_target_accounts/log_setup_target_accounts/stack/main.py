"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EventBridgeRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': 'events.amazonaws.com',
    }
    action = 'sts:AssumeRole'


@cloudformation_dataclass
class EventBridgeRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [EventBridgeRoleAllowStatement0]


@cloudformation_dataclass
class EventBridgeRole:
    """AWS::IAM::Role resource."""

    resource: iam.Role
    assume_role_policy_document = EventBridgeRoleAssumeRolePolicyDocument


@cloudformation_dataclass
class DeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    queue_name = 'CloudFormation-Logs-DLQ'


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
    targets = [{
        'Arn': ref(CentralEventBusArn),
        'RoleArn': get_att(EventBridgeRole, "Arn"),
        'Id': 'CentralEventBus',
        'DeadLetterConfig': {
            'Arn': get_att(DeadLetterQueue, "Arn"),
        },
    }]


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


@cloudformation_dataclass
class EventBridgeRolePolicyAllowStatement0:
    resource: PolicyStatement
    action = 'events:PutEvents'
    resource_arn = ref(CentralEventBusArn)


@cloudformation_dataclass
class EventBridgeRolePolicyPolicyDocument:
    resource: PolicyDocument
    statement = [EventBridgeRolePolicyAllowStatement0]


@cloudformation_dataclass
class EventBridgeRolePolicy:
    """AWS::IAM::RolePolicy resource."""

    resource: iam.RolePolicy
    policy_name = 'EventBridgeRolePolicy'
    policy_document = EventBridgeRolePolicyPolicyDocument
    role_name = ref(EventBridgeRole)
