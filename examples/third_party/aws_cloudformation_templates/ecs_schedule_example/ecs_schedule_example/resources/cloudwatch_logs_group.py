from __future__ import annotations

"""CloudwatchLogsGroup - AWS::Logs::LogGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class CloudwatchLogsGroup:
    """AWS::Logs::LogGroup resource."""

    resource: LogGroup
    log_group_name = Join('-', [
    'ECSLogGroup',
    AWS_STACK_NAME,
])
    retention_in_days = 14
    kms_key_id = ref(LogsKmsKey)
