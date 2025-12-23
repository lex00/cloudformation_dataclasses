"""CentralEventRule - AWS::Events::Rule resource."""

from .. import *  # noqa: F403


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
