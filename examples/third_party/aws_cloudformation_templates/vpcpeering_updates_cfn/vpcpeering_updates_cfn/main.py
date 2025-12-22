"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import 2RouteTableConditionCondition, 2SecurityGroupConditionCondition, 3RouteTableConditionCondition, 3SecurityGroupConditionCondition, 4RouteTableConditionCondition, 4SecurityGroupConditionCondition, 5RouteTableConditionCondition, 5SecurityGroupConditionCondition, 6RouteTableConditionCondition, 6SecurityGroupConditionCondition, NumberOfRouteTables, NumberOfSecurityGroups, PeerName, PeerVPCCIDR, RouteTableIds, SecurityGroupIds, VPCPeeringConnectionId


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
