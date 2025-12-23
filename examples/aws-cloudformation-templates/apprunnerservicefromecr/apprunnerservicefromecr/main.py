"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import ECRURL, TCPPORT
from .outputs import AppRunnerOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template AppRunnerService: This template demonstrates the creation of a App Runner Service from existing ECR Repository.  **WARNING** This template creates an AWS App Runner Service. You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[ECRURL, TCPPORT],
        outputs=[AppRunnerOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
