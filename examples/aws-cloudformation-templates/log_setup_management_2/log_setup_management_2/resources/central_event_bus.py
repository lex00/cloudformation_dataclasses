"""CentralEventBus - AWS::Events::EventBus resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CentralEventBus:
    """AWS::Events::EventBus resource."""

    resource: events.EventBus
    description = 'A custom event bus in the central account to be used as a destination for events from a rule in target accounts'
    name = ref(CentralEventBusName)
    dead_letter_config = {
        'Arn': get_att(DeadLetterQueue, "Arn"),
    }
