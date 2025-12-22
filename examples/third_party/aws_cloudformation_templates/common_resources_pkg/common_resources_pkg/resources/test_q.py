"""TestQ - AWS::SQS::Queue resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class TestQ:
    """AWS::SQS::Queue resource."""

    resource: Queue
    queue_name = 'test-events17'
