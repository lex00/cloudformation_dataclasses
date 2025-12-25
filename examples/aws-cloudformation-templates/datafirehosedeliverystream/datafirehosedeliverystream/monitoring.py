"""Monitoring resources: FirehoseLogGroup, FirehoseLogStream."""

from . import *  # noqa: F403


@cloudformation_dataclass
class FirehoseLogGroup:
    """AWS::Logs::LogGroup resource."""

    resource: logs.LogGroup
    log_group_name = Join('', [
    '/aws/kinesisfirehose/',
    ref(LogGroupName),
])
    retention_in_days = ref(CloudWatchLogGroupRetention)
    kms_key_id = If("CloudWatchLogsKMSKeyCondition", ref(CloudWatchLogsKMSKey), AWS_NO_VALUE)


@cloudformation_dataclass
class FirehoseLogStream:
    """AWS::Logs::LogStream resource."""

    resource: logs.LogStream
    log_group_name = ref(FirehoseLogGroup)
    log_stream_name = ref(LogStreamName)
