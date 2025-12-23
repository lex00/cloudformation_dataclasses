"""Template outputs and builder."""

from . import *  # noqa: F403
from .context import ctx


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='S3 bucket with encryption-required policy',
        context=ctx,  # Applies naming pattern + tags to all resources
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
