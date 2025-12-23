"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import SubnetConfigMapping, VPCName
from .outputs import DefaultSecurityGroupOutput, PrivateSubnet0Output, PrivateSubnet1Output, PublicSubnet0Output, PublicSubnet1Output, VPCIdOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Creates a VPC with Managed NAT, similar to the VPC Wizard at https://console.aws.amazon.com/vpc/home#wizardFullpagePublicAndPrivate: (extended from VPC_with_PublicIPs_And_DNS.template sample)',
        parameters=[VPCName],
        outputs=[VPCIdOutput, PublicSubnet0Output, PublicSubnet1Output, PrivateSubnet0Output, PrivateSubnet1Output, DefaultSecurityGroupOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
