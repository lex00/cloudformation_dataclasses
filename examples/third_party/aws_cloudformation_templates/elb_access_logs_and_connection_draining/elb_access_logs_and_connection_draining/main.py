"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import InstanceType, KeyName, LatestAmiId, Region2ELBAccountIdMapping, Region2ExamplesMapping, SSHLocation
from .outputs import URLOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template ELB_Access_Logs_And_Connection_Draining: Creates a load balanced, scalable sample website using Elastic Load Balancer attached to an Auto Scaling group. The ELB has connection draining enabled and also puts access logs into an S3 bucket. ** This template creates one or more Amazon EC2 instances. You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[InstanceType, KeyName, SSHLocation, LatestAmiId],
        outputs=[URLOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
