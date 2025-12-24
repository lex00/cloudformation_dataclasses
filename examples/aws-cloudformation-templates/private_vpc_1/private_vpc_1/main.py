"""Template builder."""

from . import *  # noqa: F403, F401


def build_template() -> Template:
    """Build the CloudFormation template."""
    return Template.from_registry(
        description='A stack for deploying containerized applications onto a cluster of EC2 hosts using Elastic Container Service. This stack runs containers on hosts that are in a private VPC subnet. Outbound network traffic from the hosts must go out through a NAT gateway. There are two load balancers, one inside the public subnet, which can be used to send traffic to the containers in the private subnet, and one in the private subnet, which can be used for private internal traffic between internal services.',
        parameters=[DesiredCapacity, MaxSize, ECSAMI, InstanceType],
        outputs=[ClusterNameOutput, InternalUrlOutput, ExternalUrlOutput, ECSRoleOutput, PublicListenerOutput, PrivateListenerOutput, VPCIdOutput, PublicSubnetOneOutput, PublicSubnetTwoOutput, PrivateSubnetOneOutput, PrivateSubnetTwoOutput, EcsHostSecurityGroupOutput],
    )


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json
    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
