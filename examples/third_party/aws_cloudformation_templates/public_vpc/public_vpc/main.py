"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .config import SubnetConfigMapping
from .outputs import ClusterNameOutput, ECSRoleOutput, ECSTaskExecutionRoleOutput, ExternalUrlOutput, FargateContainerSecurityGroupOutput, PublicListenerOutput, PublicSubnetOneOutput, PublicSubnetTwoOutput, VPCIdOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='A stack for deploying containerized applications in AWS Fargate. This stack runs containers in a public VPC subnet, and includes a public facing load balancer to register the services in.',
        outputs=[ClusterNameOutput, ExternalUrlOutput, ECSRoleOutput, ECSTaskExecutionRoleOutput, PublicListenerOutput, VPCIdOutput, PublicSubnetOneOutput, PublicSubnetTwoOutput, FargateContainerSecurityGroupOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
