"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Join Windows instance to AWS-Active Directory or Microsoft AD (no powershell). Create SSM document, IAM Role, SSM doc and EC2 Instance. Attaches EC2 instance to AD. Will need to use Domain Logins to RDP in.',
        parameters=[AMI, KeyPair, PublicSubnet, VPC, InstanceType, ADDirectoryId, ADDirectoryName, ADDnsIpAddresses1, ADDnsIpAddresses2],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
