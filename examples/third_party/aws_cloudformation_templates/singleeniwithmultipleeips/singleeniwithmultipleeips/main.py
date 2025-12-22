"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import Subnet


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Template Creates a single EC2 instance with a single ENI which has multiple private and public IPs',
        parameters=[Subnet],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
