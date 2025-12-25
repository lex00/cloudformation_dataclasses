"""Template builder."""

from . import *  # noqa: F403, F401
from .stack.outputs import (
    AvailabilityZonesOutput,
    PrivateSubnetIdsOutput,
    PublicSubnetIdsOutput,
    VpcCidrOutput,
    VpcIdOutput,
)


def build_template() -> Template:
    """Build the CloudFormation template."""
    template = Template.from_registry(
        description="VPC stack - network foundation for Fargate webapp",
    )
    template.add_output("VpcId", VpcIdOutput)
    template.add_output("PublicSubnetIds", PublicSubnetIdsOutput)
    template.add_output("PrivateSubnetIds", PrivateSubnetIdsOutput)
    template.add_output("AvailabilityZones", AvailabilityZonesOutput)
    template.add_output("VpcCidr", VpcCidrOutput)
    return template


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
