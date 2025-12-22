from __future__ import annotations

"""MyDeadLetterQueue - AWS::SQS::Queue resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyDeadLetterQueue:
    """AWS::SQS::Queue resource."""

    resource: Queue
    message_retention_period = 1209600
    condition = 'CreateDeadLetterQueue'
