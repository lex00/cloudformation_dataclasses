"""Macro - AWS::CloudFormation::Macro resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Macro:
    """AWS::CloudFormation::Macro resource."""

    # Unknown resource type: AWS::CloudFormation::Macro
    resource: CloudFormationResource
    name = 'Count'
    function_name = get_att(CountMacroFunction, "Arn")
