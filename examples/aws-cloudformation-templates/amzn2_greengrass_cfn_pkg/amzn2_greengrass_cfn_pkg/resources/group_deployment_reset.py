"""GroupDeploymentReset - Custom::GroupDeploymentReset resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GroupDeploymentReset:
    """Custom::GroupDeploymentReset resource."""

    # Unknown resource type: Custom::GroupDeploymentReset
    resource: CloudFormationResource
    region = AWS_REGION
    service_token = get_att(GroupDeploymentResetFunction, "Arn")
    thing_name = Join('_', [
    ref(CoreName),
    'Core',
])
    depends_on = ["GreengrassGroup"]
