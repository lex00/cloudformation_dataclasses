from __future__ import annotations

"""CentralEventLog - AWS::Logs::LogGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CentralEventLog:
    """AWS::Logs::LogGroup resource."""

    resource: LogGroup
    log_group_class = 'STANDARD'
    log_group_name = ref(CentralEventLogName)
    kms_key_id: GetAtt[CentralEventLogKey] = get_att("Arn")
    depends_on = ["CentralEventBus"]
