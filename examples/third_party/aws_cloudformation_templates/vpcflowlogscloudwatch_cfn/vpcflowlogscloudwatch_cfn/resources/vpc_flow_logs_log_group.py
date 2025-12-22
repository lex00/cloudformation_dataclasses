"""VPCFlowLogsLogGroup - AWS::Logs::LogGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class VPCFlowLogsLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: LogGroup
    retention_in_days = ref(VPCFlowLogsLogGroupRetention)
    kms_key_id = If("VPCFlowLogsCloudWatchKMSKeyCondition", ref(VPCFlowLogsCloudWatchKMSKey), AWS_NO_VALUE)
