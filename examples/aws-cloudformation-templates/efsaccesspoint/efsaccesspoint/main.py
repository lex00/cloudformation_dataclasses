"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import AccessPointName, EFSFileSystemName, SecurityGroup1, SecurityGroup2, SecurityGroup3, Subnet1, Subnet2, Subnet3
from .outputs import FileSystemIdOutput


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
