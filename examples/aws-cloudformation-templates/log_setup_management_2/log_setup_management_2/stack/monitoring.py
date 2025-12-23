"""Monitoring resources: CentralEventLog, CentralEventLogQuery, CentralEventLogQueryReason, CentralEventLogPolicy."""

from .. import *  # noqa: F403


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
