"""Template builder."""

from . import *  # noqa: F403, F401
from .stack.params import DomainNameParam
from .stack.outputs import (
    CertificateArnOutput,
    HostedZoneIdOutput,
    NameServersOutput,
)


def build_template() -> Template:
    """Build the CloudFormation template."""
    template = Template.from_registry(
        description="DNS stack - Route53 hosted zone and ACM certificate",
    )
    template.add_parameter("DomainName", DomainNameParam)
    template.add_output("HostedZoneId", HostedZoneIdOutput)
    template.add_output("CertificateArn", CertificateArnOutput)
    template.add_output("NameServers", NameServersOutput)
    return template


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
