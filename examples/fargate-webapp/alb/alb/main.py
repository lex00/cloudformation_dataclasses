"""Template builder."""

from . import *  # noqa: F403, F401
from .stack.params import (
    CertificateArnParam,
    DomainNameParam,
    HostedZoneIdParam,
    PublicSubnetIdsParam,
    VpcIdParam,
)
from .stack.outputs import (
    AlbArnOutput,
    AlbDnsNameOutput,
    AlbSecurityGroupIdOutput,
    HttpsListenerArnOutput,
    TargetGroupArnOutput,
)


def build_template() -> Template:
    """Build the CloudFormation template."""
    template = Template.from_registry(
        description="ALB stack - Application Load Balancer with HTTPS",
    )
    template.add_parameter("VpcId", VpcIdParam)
    template.add_parameter("PublicSubnetIds", PublicSubnetIdsParam)
    template.add_parameter("CertificateArn", CertificateArnParam)
    template.add_parameter("HostedZoneId", HostedZoneIdParam)
    template.add_parameter("DomainName", DomainNameParam)
    template.add_output("AlbArn", AlbArnOutput)
    template.add_output("AlbDnsName", AlbDnsNameOutput)
    template.add_output("AlbSecurityGroupId", AlbSecurityGroupIdOutput)
    template.add_output("TargetGroupArn", TargetGroupArnOutput)
    template.add_output("HttpsListenerArn", HttpsListenerArnOutput)
    return template


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
