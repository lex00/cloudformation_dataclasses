"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""Sample template showing how to create an instance with a single network
interface and multiple static IP addresses in an existing VPC. It assumes you
have already created a VPC.  **WARNING** This template creates an Amazon EC2
instance. You will be billed for the AWS resources used if you create a stack
from this template.
""",
        parameters=[KeyName, InstanceType, VpcId, SubnetId, PrimaryIPAddress, SecondaryIPAddress, SSHLocation, LatestAMI],
        outputs=[InstanceIdOutput, EIP1Output, PrimaryPrivateIPAddressOutput, SecondaryPrivateIPAddressesOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
