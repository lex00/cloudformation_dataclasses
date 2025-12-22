"""FirehoseLogStream - AWS::Logs::LogStream resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class FirehoseLogStream:
    """AWS::Logs::LogStream resource."""

    resource: LogStream
    log_group_name = ref(FirehoseLogGroup)
    log_stream_name = ref(LogStreamName)
