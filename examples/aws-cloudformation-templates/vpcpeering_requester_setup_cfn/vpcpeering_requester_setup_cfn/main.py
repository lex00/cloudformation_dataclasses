"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This templates creates a VPC Peering connection. (Requester Account)',
        parameters=[PeerName, PeerOwnerId, PeerRoleARN, PeerVPCID, VPCID],
        outputs=[VPCPeeringConnectionIdOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
