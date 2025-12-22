from __future__ import annotations

"""DeadLetterQueue - AWS::SQS::Queue resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class DeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: Queue
    queue_name = 'CloudFormation-Logs-DLQ'
