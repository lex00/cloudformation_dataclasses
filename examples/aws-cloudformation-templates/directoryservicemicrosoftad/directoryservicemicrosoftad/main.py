"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import cAliasCondition, pCreateAlias, pDomainName, pEdition, pEnableSingleSignOn, pMicrosoftADShortName, pPrivateSubnet1, pPrivateSubnet2, pVPCID
from .outputs import DirectoryAliasOutput, DirectoryIDOutput, PrimaryDNSOutput, SecondaryDNSOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""Provision AWS Managed Active Directory
""",
        parameters=[pEdition, pDomainName, pMicrosoftADShortName, pEnableSingleSignOn, pCreateAlias, pPrivateSubnet1, pPrivateSubnet2, pVPCID],
        outputs=[DirectoryIDOutput, PrimaryDNSOutput, SecondaryDNSOutput, DirectoryAliasOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
