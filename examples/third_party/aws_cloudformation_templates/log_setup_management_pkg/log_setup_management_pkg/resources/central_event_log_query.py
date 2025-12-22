from __future__ import annotations

"""CentralEventLogQuery - AWS::Logs::QueryDefinition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CentralEventLogQuery:
    """AWS::Logs::QueryDefinition resource."""

    resource: QueryDefinition
    name = 'CentralCloudFormationEventLogs'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` | sort @timestamp desc'
    log_group_names = [ref(CentralEventLogName)]
