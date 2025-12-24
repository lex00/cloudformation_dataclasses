"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template AutoScalingScheduledAction: Create a load balanced, Auto Scaled sample website. This example creates an Auto Scaling group with time-based scheduled actions behind a load balancer with a simple health check. **WARNING** This template creates one or more Amazon EC2 instances and an Elastic Load Balancer. You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[InstanceType, KeyName, SSHLocation],
        outputs=[URLOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
