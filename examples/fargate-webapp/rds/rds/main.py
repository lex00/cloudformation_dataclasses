"""Template builder."""

from . import *  # noqa: F403, F401
from .stack.params import (
    DatabaseNameParam,
    PrivateSubnetIdsParam,
    VpcCidrParam,
    VpcIdParam,
)
from .stack.outputs import (
    DbEndpointOutput,
    DbPortOutput,
    DbSecretArnOutput,
    DbSecurityGroupIdOutput,
)


def build_template() -> Template:
    """Build the CloudFormation template."""
    template = Template.from_registry(
        description="RDS stack - PostgreSQL database with Secrets Manager",
    )
    template.add_parameter("VpcId", VpcIdParam)
    template.add_parameter("PrivateSubnetIds", PrivateSubnetIdsParam)
    template.add_parameter("VpcCidr", VpcCidrParam)
    template.add_parameter("DatabaseName", DatabaseNameParam)
    template.add_output("DbEndpoint", DbEndpointOutput)
    template.add_output("DbPort", DbPortOutput)
    template.add_output("DbSecretArn", DbSecretArnOutput)
    template.add_output("DbSecurityGroupId", DbSecurityGroupIdOutput)
    return template


def main() -> None:
    """Print the CloudFormation template as JSON."""
    import json

    template = build_template()
    print(json.dumps(template.to_dict(), indent=2))


if __name__ == "__main__":
    main()
