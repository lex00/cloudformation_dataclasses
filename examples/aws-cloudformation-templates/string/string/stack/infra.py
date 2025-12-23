"""Infra resources: Transform."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Transform:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = 'String'
    description = 'Provides various string processing functions'
    function_name = get_att(TransformFunction, "Arn")
