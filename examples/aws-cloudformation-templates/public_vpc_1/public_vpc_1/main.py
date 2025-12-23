"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import DesiredCapacity, ECSAMI, InstanceType, MaxSize, SubnetConfigMapping
from .outputs import ClusterNameOutput, ECSRoleOutput, EcsHostSecurityGroupOutput, ExternalUrlOutput, PublicListenerOutput, PublicSubnetOneOutput, PublicSubnetTwoOutput, VPCIdOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='A stack for deploying containerized applications onto a cluster of EC2 hosts using Elastic Container Service. This stack runs containers on hosts that are in a public VPC subnet, and includes a public facing load balancer to register the services in.',
        parameters=[DesiredCapacity, MaxSize, ECSAMI, InstanceType],
        outputs=[ClusterNameOutput, ExternalUrlOutput, ECSRoleOutput, PublicListenerOutput, VPCIdOutput, PublicSubnetOneOutput, PublicSubnetTwoOutput, EcsHostSecurityGroupOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
