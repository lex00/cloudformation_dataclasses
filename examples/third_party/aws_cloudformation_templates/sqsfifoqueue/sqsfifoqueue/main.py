"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import ContentBasedDeduplication, CreateDeadLetterQueueCondition, MaximumMessageSize, MessageRetentionPeriod, QueueName, ReceiveMessageWaitTimeSeconds, UsedeadletterQueue, VisibilityTimeout
from .outputs import QueueARNOutput, QueueNameOutput, QueueURLOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Best Practice SQS FIFO Queue, only available in us-east-1, us-east-2, us-west-2, eu-west-1, ap-northeast-1, ap-southeast-2 at time of template creation.',
        parameters=[ContentBasedDeduplication, QueueName, MaximumMessageSize, MessageRetentionPeriod, ReceiveMessageWaitTimeSeconds, UsedeadletterQueue, VisibilityTimeout],
        outputs=[QueueURLOutput, QueueARNOutput, QueueNameOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
