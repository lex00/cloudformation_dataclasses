from __future__ import annotations

"""CloudFormationEventRule - AWS::Events::Rule resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudFormationEventRuleDeadLetterConfig:
    resource: DeadLetterConfig
    arn = get_att(DeadLetterQueue, "Arn")


@cloudformation_dataclass
class CloudFormationEventRuleTarget:
    resource: Target
    arn = ref(CentralEventBusArn)
    role_arn = get_att(EventBridgeRole, "Arn")
    id = 'CentralEventBus'
    dead_letter_config = CloudFormationEventRuleDeadLetterConfig


@cloudformation_dataclass
class CloudFormationEventRule:
    """AWS::Events::Rule resource."""

    resource: Rule
    name = 'CloudFormationEventRule'
    event_bus_name = Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/default')
    event_pattern = {
        'source': ['aws.cloudformation'],
    }
    state = 'ENABLED'
    targets = [CloudFormationEventRuleTarget]
