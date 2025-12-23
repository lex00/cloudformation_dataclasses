"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""Create a multi-az, load balanced and Auto Scaled sample web site running on
an Apache Web Server. The application is configured to span all
Availability Zones in the region and is Auto-Scaled based on the CPU
utilization of the web servers. Notifications will be sent to the operator
email address on scaling events. The instances are load balanced with a
simple health check against the default web page. **WARNING** This template
creates one or more Amazon EC2 instances and an Elastic Load Balancer. You
will be billed for the AWS resources used if you create a stack from this
template.
""",
        parameters=[InstanceType, OperatorEMail, KeyName, SSHLocation, LatestAmiId, KmsKeyArn, CertificateArn, SecurityGroups, Subnets, AZs, VPC],
        outputs=[URLOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
