"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import NumberOfRouteTables, NumberOfSecurityGroups, PeerName, PeerVPCCIDR, RouteTableIds, SecurityGroupIds, VPCPeeringConnectionId, _2RouteTableConditionCondition, _2SecurityGroupConditionCondition, _3RouteTableConditionCondition, _3SecurityGroupConditionCondition, _4RouteTableConditionCondition, _4SecurityGroupConditionCondition, _5RouteTableConditionCondition, _5SecurityGroupConditionCondition, _6RouteTableConditionCondition, _6SecurityGroupConditionCondition


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
