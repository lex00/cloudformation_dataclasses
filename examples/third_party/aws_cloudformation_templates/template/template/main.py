"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import EKSClusterVersion, NodeGroupInstanceTypes, PrivateCidrBlock1, PrivateCidrBlock2, PrivateCidrBlock3, PublicCidrBlock1, PublicCidrBlock2, PublicCidrBlock3, ServicePrincipalPartitionMapMapping, VPCCidrBlock


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='AWS CloudFormation Sample Template EKS Cluster on EC2',
        parameters=[VPCCidrBlock, PublicCidrBlock1, PublicCidrBlock2, PublicCidrBlock3, PrivateCidrBlock1, PrivateCidrBlock2, PrivateCidrBlock3, EKSClusterVersion, NodeGroupInstanceTypes],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
