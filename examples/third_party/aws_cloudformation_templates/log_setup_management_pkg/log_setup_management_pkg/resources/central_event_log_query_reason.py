"""CentralEventLogQueryReason - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CentralEventLogQueryReason:
    """AWS::Logs::QueryDefinition resource."""

    resource: QueryDefinition
    name = 'CentralCloudFormationFailures'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` as status, `detail.status-details.status-reason` as reason | sort @timestamp desc | filter status like "FAILED" | filter reason not like "canceled" | filter resource not like "AWS::CloudFormation::Stack" '
    log_group_names = [ref(CentralEventLogName)]
