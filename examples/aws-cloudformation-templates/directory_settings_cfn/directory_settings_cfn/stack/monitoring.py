"""Monitoring resources: DirectorySettingsLambdaLogsLogGroup."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DirectorySettingsLambdaLogsLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_name = Sub('/aws/lambda/${LambdaFunctionName}')
    retention_in_days = ref(LambdaLogsLogGroupRetention)
    kms_key_id = If("LambdaLogsCloudWatchKMSKeyCondition", ref(LambdaLogsCloudWatchKMSKey), AWS_NO_VALUE)
