"""Template outputs."""

from . import *  # noqa: F403


@cloudformation_dataclass
class ExecutionRoleArnOutput:
    """ARN of the StackSet execution role"""

    resource: Output
    value = get_att("AWSCloudFormationStackSetExecutionRole", "Arn")
    description = 'ARN of the StackSet execution role'
