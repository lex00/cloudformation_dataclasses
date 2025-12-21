from __future__ import annotations

"""Macro - AWS::CloudFormation::Macro resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = 'StackMetrics'
    function_name: GetAtt[MacroFunction] = get_att("Arn")
