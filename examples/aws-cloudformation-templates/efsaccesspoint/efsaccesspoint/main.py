"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='Creates an EFS file system with three mount targets and one access point.',
        parameters=[EFSFileSystemName, AccessPointName, Subnet1, Subnet2, Subnet3, SecurityGroup1, SecurityGroup2, SecurityGroup3],
        outputs=[FileSystemIdOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
