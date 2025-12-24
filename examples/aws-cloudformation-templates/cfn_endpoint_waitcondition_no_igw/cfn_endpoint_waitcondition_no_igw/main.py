"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""This template deploys a VPC with a pair of private subnets spread across two Availabilty Zones. It deploys VPC Endpoints for CloudFormation and S3 so an instance in the private subnet can use cfn-signal for a WaitCondition. **WARNING** You will be billed for the AWS resources used if you create a stack from this template.
""",
        parameters=[EnvironmentName, VpcCIDR, PrivateSubnet1CIDR, PrivateSubnet2CIDR, LinuxAMI],
        outputs=[VPCOutput, PrivateSubnetsOutput, CfnEndpointOutput, S3EndpointOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
