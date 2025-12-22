"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class AdministrationRoleArnOutput:
    """ARN of the StackSet administration role"""

    resource: Output
    value = get_att(AWSCloudFormationStackSetAdministrationRole, "Arn")
    description = 'ARN of the StackSet administration role'
    export_name = 'StackSetAdministrationRoleArn'
