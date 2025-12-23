"""CentralEventLog - AWS::Logs::LogGroup resource."""

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
