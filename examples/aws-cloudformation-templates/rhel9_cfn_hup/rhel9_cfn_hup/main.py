"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import AWSInstanceType2ArchMapping, AWSRegionArch2AMIMapping, InstanceType, KeyName, SSHLocation, SubnetId


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Installing Cloudformation helper scripts in RHEL 9',
        parameters=[KeyName, InstanceType, SSHLocation, SubnetId],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
