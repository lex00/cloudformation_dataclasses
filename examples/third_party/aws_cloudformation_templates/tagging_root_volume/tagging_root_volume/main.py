"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import InstanceAZ, InstanceType, KeyName, LinuxAMIID, SubnetId, WindowsAMIID


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template Tagging Root Volumes of EC2 Instances: This template shows how to automatically tag the root volume of the EC2 instances which are created through the CloudFormation template. This is done through the UserData property of the AWS::EC2::Instance resource. **WARNING** This template creates two Amazon EC2 instances and an IAM Role. You will be billed for the AWS resources used if you create a stack from this template.',
        parameters=[KeyName, InstanceType, InstanceAZ, WindowsAMIID, LinuxAMIID, SubnetId],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
