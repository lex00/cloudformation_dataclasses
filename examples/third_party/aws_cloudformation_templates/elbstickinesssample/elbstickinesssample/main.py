"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import InstanceType, KeyName, LatestAmiId, Region2ExamplesMapping, SSHLocation, SubnetId
from .outputs import URLOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template ELBStickinessSample: Create a load balanced sample web site with ELB stickiness enabled. The AI is chosen based on the region in which the stack is run. This example creates 2 EC2 instances behind a load balancer with a simple health check. The ec2 instances are untargeted and may be deployed in one or more availaiblity zones. The web site is available on port 80, however, the instances can be configured to listen on any port (8888 by default). **WARNING** This template creates one or more Amazon EC2 instances and an Elastic Load Balancer. You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[LatestAmiId, InstanceType, KeyName, SSHLocation, SubnetId],
        outputs=[URLOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
