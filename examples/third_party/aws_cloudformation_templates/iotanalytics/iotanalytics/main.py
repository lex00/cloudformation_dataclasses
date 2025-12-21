"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import ProjectName, ScheduleExpression, SqlQuery


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template Config: This template creates a Channel, Datastore, Pipeline and Dataset with SQL action. **WARNING** You will be billed for the AWS resources used if you create a stack from this template. See https://aws.amazon.com/blogs/iot/introducing-aws-cloudformation-support-for-aws-iot-analytics/ for further details.',
        parameters=[ProjectName, SqlQuery, ScheduleExpression],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
