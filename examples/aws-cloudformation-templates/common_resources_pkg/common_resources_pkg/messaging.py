"""Messaging resources: TestQ."""

from . import *  # noqa: F403


@cloudformation_dataclass
class TestQ:
    """AWS::SQS::Queue resource."""

    resource: sqs.Queue
    queue_name = 'test-events17'
