"""FirehoseLogGroup - AWS::Logs::LogGroup resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class FirehoseLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: LogGroup
    log_group_name = Join('', [
    '/aws/kinesisfirehose/',
    ref(LogGroupName),
])
    retention_in_days = ref(CloudWatchLogGroupRetention)
    kms_key_id = If("CloudWatchLogsKMSKeyCondition", ref(CloudWatchLogsKMSKey), AWS_NO_VALUE)
