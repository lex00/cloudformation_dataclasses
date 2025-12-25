"""Template builder."""

from . import *  # noqa: F403, F401
from .stack.params import (
    AlbSecurityGroupIdParam,
    DbEndpointParam,
    DbSecretArnParam,
    PrivateSubnetIdsParam,
    TargetGroupArnParam,
    VpcIdParam,
)
from .stack.outputs import (
    ClusterArnOutput,
    ServiceArnOutput,
    ServiceNameOutput,
)


def build_template() -> Template:
    """Build the CloudFormation template."""
    template = Template.from_registry(
        description="Fargate stack - ECS service with task definition",
    )
    template.add_parameter("VpcId", VpcIdParam)
    template.add_parameter("PrivateSubnetIds", PrivateSubnetIdsParam)
    template.add_parameter("AlbSecurityGroupId", AlbSecurityGroupIdParam)
    template.add_parameter("TargetGroupArn", TargetGroupArnParam)
    template.add_parameter("DbEndpoint", DbEndpointParam)
    template.add_parameter("DbSecretArn", DbSecretArnParam)
    template.add_output("ClusterArn", ClusterArnOutput)
    template.add_output("ServiceName", ServiceNameOutput)
    template.add_output("ServiceArn", ServiceArnOutput)
    return template


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
