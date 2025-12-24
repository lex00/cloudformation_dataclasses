"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template updates the specified route tables & security groups to allow communications via the VPC peering connection.',
        parameters=[NumberOfRouteTables, NumberOfSecurityGroups, PeerName, PeerVPCCIDR, RouteTableIds, SecurityGroupIds, VPCPeeringConnectionId],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
