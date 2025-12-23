"""Messaging resources: DeadLetterQueue, CentralEventBus, CentralEventBusPolicy, CentralEventRule."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    queue_name = Sub('${CentralEventBusName}-DLQ')


@cloudformation_dataclass
class CentralEventBus:
    """AWS::Events::EventBus resource."""

    resource: events.EventBus
    description = 'A custom event bus in the central account to be used as a destination for events from a rule in target accounts'
    name = ref(CentralEventBusName)
    dead_letter_config = {
        'Arn': get_att(DeadLetterQueue, "Arn"),
    }


@cloudformation_dataclass
class CentralEventBusPolicy:
    """AWS::Events::EventBusPolicy resource."""

    resource: events.EventBusPolicy
    event_bus_name = ref(CentralEventBus)
    statement_id = 'CentralEventBusPolicyStatement'
    statement = {
        'Effect': 'Allow',
        'Principal': '*',
        'Action': 'events:PutEvents',
        'Resource': Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/${CentralEventBusName}'),
        'Condition': {
            'StringEquals': {
                'aws:PrincipalOrgID': ref(OrgID),
            },
        },
    }


@cloudformation_dataclass
class CentralEventRule:
    """AWS::Events::Rule resource."""

    resource: events.Rule
    name = 'CloudFormationLogs'
    event_bus_name = ref(CentralEventBusName)
    state = 'ENABLED'
    event_pattern = {
        'source': [{
            'prefix': '',
        }],
    }
    targets = [{
        'Arn': get_att(CentralEventLog, "Arn"),
        'Id': 'CloudFormationLogsToCentralGroup',
        'DeadLetterConfig': {
            'Arn': get_att(DeadLetterQueue, "Arn"),
        },
    }]
    depends_on = ["CentralEventLog"]
