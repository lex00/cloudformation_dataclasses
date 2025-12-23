"""Template outputs and builder."""

from . import *  # noqa: F403
from .resources import *  # noqa: F403, F401
from .stack_config import SubnetConfigMapping
from .outputs import ClusterNameOutput, ECSRoleOutput, ECSTaskExecutionRoleOutput, ExternalUrlOutput, FargateContainerSecurityGroupOutput, InternalUrlOutput, PrivateListenerOutput, PrivateSubnetOneOutput, PrivateSubnetTwoOutput, PublicListenerOutput, PublicSubnetOneOutput, PublicSubnetTwoOutput, VPCIdOutput


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='This stack deploys a Fargate cluster that is in a VPC with both public and private subnets. Containers can be deployed into either the public subnets or the private subnets, and there are two load balancers. One is inside the public subnet, which can be used to send traffic to the containers in the private subnet, and one in the private subnet, which can be used for private internal traffic between internal services.',
        outputs=[ClusterNameOutput, InternalUrlOutput, ExternalUrlOutput, ECSRoleOutput, ECSTaskExecutionRoleOutput, PublicListenerOutput, PrivateListenerOutput, VPCIdOutput, PublicSubnetOneOutput, PublicSubnetTwoOutput, PrivateSubnetOneOutput, PrivateSubnetTwoOutput, FargateContainerSecurityGroupOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
