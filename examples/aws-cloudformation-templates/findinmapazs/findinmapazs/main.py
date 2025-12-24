"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This template deploys a VPC, with a pair of public and private subnets spread across two Availability Zones. It uses a static AZ Mapping known as RegionMap to ensure that your resources persist in a given Availability Zone if we add or remove zones',
        parameters=[VpcCIDR, PublicSubnet1CIDR, PublicSubnet2CIDR, PrivateSubnet1CIDR, PrivateSubnet2CIDR],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
