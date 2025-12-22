"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import LogGroupName, NatGatewayID, NatGatewayPrivateIP, VpcCidr
from .outputs import DashboardArnOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Creates a CloudWatch Dashboard with four CloudWatch Logs Insights log widgets that query VPC flow logs for NAT Gateway, related to https://repost.aws/knowledge-center/vpc-find-traffic-sources-nat-gateway',
        parameters=[NatGatewayPrivateIP, NatGatewayID, VpcCidr, LogGroupName],
        outputs=[DashboardArnOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
