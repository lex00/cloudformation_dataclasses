from __future__ import annotations

"""Macro - AWS::CloudFormation::Macro resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = 'Count'
    function_name: GetAtt[CountMacroFunction] = get_att("Arn")
