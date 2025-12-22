from __future__ import annotations

"""CentralEventRule - AWS::Events::Rule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CentralEventRuleDeadLetterConfig:
    resource: DeadLetterConfig
    arn: GetAtt[DeadLetterQueue] = get_att("Arn")


@cloudformation_dataclass
class CentralEventRuleTarget:
    resource: Target
    arn: GetAtt[CentralEventLog] = get_att("Arn")
    id = 'CloudFormationLogsToCentralGroup'
    dead_letter_config = CentralEventRuleDeadLetterConfig


@cloudformation_dataclass
class CentralEventRule:
    """AWS::Events::Rule resource."""

    resource: Rule
    name = 'CloudFormationLogs'
    event_bus_name = ref(CentralEventBusName)
    state = 'ENABLED'
    event_pattern = {
        'source': [{
            'prefix': '',
        }],
    }
    targets = [CentralEventRuleTarget]
    depends_on = ["CentralEventLog"]
