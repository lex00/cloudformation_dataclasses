"""Infra resources: Macro."""

from . import *  # noqa: F403


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = 'StackMetrics'
    function_name = get_att(MacroFunction, "Arn")
