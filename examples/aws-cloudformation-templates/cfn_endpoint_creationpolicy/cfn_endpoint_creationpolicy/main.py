"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""This template deploys a VPC with a pair of public and private subnets spread across two Availabilty Zones. It deploys an Internet Gateway, with a default route on the public subnets and a bastion server. It deploys a VPC Endpoint for CloudFormation so an instance in the private subnet can use cfn-signal for its CreationPolicy. **WARNING** You will be billed for the AWS resources used if you create a stack from this template.
""",
        parameters=[EnvironmentName, VpcCIDR, PublicSubnet1CIDR, PublicSubnet2CIDR, PrivateSubnet1CIDR, PrivateSubnet2CIDR, KeyName, LinuxAMI],
        outputs=[VPCOutput, PublicSubnetsOutput, PrivateSubnetsOutput, CfnEndpointOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
