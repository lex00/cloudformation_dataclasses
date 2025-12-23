"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import PeerName, PeerOwnerId, PeerRoleARN, PeerRoleConditionCondition, PeerVPCID, VPCID
from .outputs import VPCPeeringConnectionIdOutput


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
