"""Infra resources: Transform."""

from . import *  # noqa: F403


@cloudformation_dataclass
class Transform:
    """AWS::CloudFormation::Macro resource."""

    resource: cloudformation.Macro
    name = Sub('PyPlate')
    description = 'Processes inline python in templates'
    function_name = get_att(TransformFunction, "Arn")
