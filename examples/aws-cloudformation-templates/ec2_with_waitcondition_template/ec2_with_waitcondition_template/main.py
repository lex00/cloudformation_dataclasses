"""Template builder."""

from . import *  # noqa: F403, F401


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
