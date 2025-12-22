"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import CentOSVersion, IAMRole, InstanceType, KeyName, RegionMapMapping, SSHLocation, SSMKey, SubnetId


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Template to install CloudWatchAgent on centos. It was validated on centos 7',
        parameters=[SSMKey, KeyName, InstanceType, CentOSVersion, IAMRole, SSHLocation, SubnetId],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
