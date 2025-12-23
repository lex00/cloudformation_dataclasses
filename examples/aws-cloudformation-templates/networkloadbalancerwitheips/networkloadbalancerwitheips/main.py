"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import ELBIpAddressType, ELBType, Subnet1, Subnet2, VPC


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Template creates a Network Load Balancer in 2 AZs with EIPs listening on TCP port 80. There are no registered targets these would either be EC2 instance IDs added to the targets property of the target group  or defined under the autoscaling group resources  ',
        parameters=[VPC, Subnet1, Subnet2, ELBType, ELBIpAddressType],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
