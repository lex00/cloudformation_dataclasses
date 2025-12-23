"""CentralEventBusPolicy - AWS::Events::EventBusPolicy resource."""

from .. import *  # noqa: F403


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
