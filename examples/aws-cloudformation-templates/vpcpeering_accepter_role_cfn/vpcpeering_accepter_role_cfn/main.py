"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template creates an assumable role to be used by the requester account to accept the VPC peering connection. (Accepter Account)',
        parameters=[PeerOwnerIds],
        outputs=[PeerRoleARNOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
