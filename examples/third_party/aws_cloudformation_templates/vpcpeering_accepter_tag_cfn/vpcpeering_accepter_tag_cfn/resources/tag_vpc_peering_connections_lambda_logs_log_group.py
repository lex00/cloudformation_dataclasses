from __future__ import annotations

"""TagVpcPeeringConnectionsLambdaLogsLogGroup - AWS::Logs::LogGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TagVpcPeeringConnectionsLambdaLogsLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: LogGroup
    log_group_name = Sub('/aws/lambda/${LambdaFunctionName}')
    retention_in_days = ref(LambdaLogsLogGroupRetention)
    kms_key_id = If("LambdaLogsCloudWatchKMSKeyCondition", ref(LambdaLogsCloudWatchKMSKey), AWS_NO_VALUE)
