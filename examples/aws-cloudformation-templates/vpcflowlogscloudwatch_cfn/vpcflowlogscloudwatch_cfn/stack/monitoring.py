"""Monitoring resources: VPCFlowLogsLogGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    retention_in_days = ref(VPCFlowLogsLogGroupRetention)
    kms_key_id = If("VPCFlowLogsCloudWatchKMSKeyCondition", ref(VPCFlowLogsCloudWatchKMSKey), AWS_NO_VALUE)
