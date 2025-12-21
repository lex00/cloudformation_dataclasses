from __future__ import annotations

"""CentralEventBusPolicy - AWS::Events::EventBusPolicy resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CentralEventBusPolicy:
    """AWS::Events::EventBusPolicy resource."""

    resource: EventBusPolicy
    event_bus_name: Ref[CentralEventBus] = ref()
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
