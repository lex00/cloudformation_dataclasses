"""CloudFormationEventRule - AWS::Events::Rule resource."""

from .. import *  # noqa: F403


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
