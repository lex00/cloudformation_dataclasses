"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import CertificateARN


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Creates required AWS resources',
        parameters=[CertificateARN],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
