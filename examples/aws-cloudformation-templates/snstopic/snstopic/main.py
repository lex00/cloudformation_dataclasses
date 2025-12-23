"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import SubscriptionEndPoint, SubscriptionProtocol
from .outputs import QueueNameOutput, TopicARNOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Best Practice SNS Topic',
        parameters=[SubscriptionEndPoint, SubscriptionProtocol],
        outputs=[TopicARNOutput, QueueNameOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
