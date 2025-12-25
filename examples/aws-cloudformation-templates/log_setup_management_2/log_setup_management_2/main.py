"""Stack resources."""

from . import *  # noqa: F403

from cloudformation_dataclasses.core.constants import STRING_EQUALS


@cloudformation_dataclass
class DeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    queue_name = Sub('${CentralEventBusName}-DLQ')
    kms_master_key_id = ref(KmsKeyId)


@cloudformation_dataclass
class CentralEventBusDeadLetterConfig:
    resource: events.event_bus.DeadLetterConfig
    arn = get_att(DeadLetterQueue, "Arn")


@cloudformation_dataclass
class CentralEventBus:
    """AWS::Events::EventBus resource."""

    resource: events.EventBus
    description = 'A custom event bus in the central account to be used as a destination for events from a rule in target accounts'
    name = ref(CentralEventBusName)
    dead_letter_config = CentralEventBusDeadLetterConfig


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
            STRING_EQUALS: {
                'aws:PrincipalOrgID': ref(OrgID),
            },
        },
    }


@cloudformation_dataclass
class CentralEventLog:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_class = 'STANDARD'
    log_group_name = ref(CentralEventLogName)
    kms_key_id = get_att(CentralEventLogKey, "Arn")
    retention_in_days = 90
    depends_on = ["CentralEventBus"]


@cloudformation_dataclass
class CentralEventLogQuery:
    """AWS::Logs::QueryDefinition resource."""

    resource: logs.QueryDefinition
    name = 'CentralCloudFormationEventLogs'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` | sort @timestamp desc'
    log_group_names = [ref(CentralEventLogName)]


@cloudformation_dataclass
class CentralEventLogQueryReason:
    """AWS::Logs::QueryDefinition resource."""

    resource: logs.QueryDefinition
    name = 'CentralCloudFormationFailures'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` as status, `detail.status-details.status-reason` as reason | sort @timestamp desc | filter status like "FAILED" | filter reason not like "canceled" | filter resource not like "AWS::CloudFormation::Stack" '
    log_group_names = [ref(CentralEventLogName)]


@cloudformation_dataclass
class CentralEventLogPolicy:
    """AWS::Logs::ResourcePolicy resource."""

    resource: logs.ResourcePolicy
    policy_name = 'CentralEventLogResourcePolicy'
    policy_document = Sub("""{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "delivery.logs.amazonaws.com",
          "events.amazonaws.com"
        ]
      },
      "Action": [
        "logs:PutLogEvents",
        "logs:CreateLogStream"
      ],
      "Resource": "${CentralEventLog.Arn}"
    }
  ]
}
""")


@cloudformation_dataclass
class CentralEventRuleDeadLetterConfig:
    resource: events.rule.DeadLetterConfig
    arn = get_att(DeadLetterQueue, "Arn")


@cloudformation_dataclass
class CentralEventRuleTarget:
    resource: events.rule.Target
    arn = get_att(CentralEventLog, "Arn")
    id = 'CloudFormationLogsToCentralGroup'
    dead_letter_config = CentralEventRuleDeadLetterConfig


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
    targets = [CentralEventRuleTarget]
    depends_on = ["CentralEventLog"]
