"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import AliasCondition, CreateAlias, DomainName, PrivateSubnet1, PrivateSubnet2, SimpleADShortName, Size, VPCID
from .outputs import DirectoryAliasOutput, DirectoryIDOutput, PrimaryDNSOutput, SecondaryDNSOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        parameters=[DomainName, SimpleADShortName, CreateAlias, PrivateSubnet1, PrivateSubnet2, VPCID, Size],
        outputs=[DirectoryIDOutput, PrimaryDNSOutput, SecondaryDNSOutput, DirectoryAliasOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
