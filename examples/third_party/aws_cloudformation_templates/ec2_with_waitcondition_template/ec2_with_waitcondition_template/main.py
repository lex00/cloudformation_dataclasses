"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import AgentID, BudgetCode, ImageId, InstanceName, InstanceType, IsMaster, KeyName, LaunchPlatform, LaunchUser, MasterID, SSHLocation, SubnetId, TestID, TestTarget, VpcId
from .outputs import InstanceIdOutput, WebsiteURLOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Create a variable number of EC2 instance resources.',
        parameters=[KeyName, InstanceName, InstanceType, ImageId, VpcId, SubnetId, SSHLocation, BudgetCode, LaunchPlatform, LaunchUser, TestID, TestTarget, AgentID, IsMaster, MasterID],
        outputs=[WebsiteURLOutput, InstanceIdOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
