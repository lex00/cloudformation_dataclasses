"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description="""This module creates an ELBv2 load balancer
""",
        parameters=[CertificateArn, VPCId, PublicSubnet1, PublicSubnet2, DestinationSecurityGroupId],
        outputs=[LoadBalancerDNSOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
