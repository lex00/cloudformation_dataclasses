"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Create Greengrass resources and group, with supporting AWS services. See https://aws.amazon.com/blogs/iot/automating-aws-iot-greengrass-setup-with-aws-cloudformation/ for further details.',
        parameters=[CoreName, SecurityAccessCIDR, myKeyPair, LatestAmiId, InstanceType],
        outputs=[EC2IPAddressOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
