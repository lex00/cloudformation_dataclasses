"""Infra resources: Transform."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Transform:
    """AWS::CloudFormation::Macro resource."""

    # Unknown resource type: AWS::CloudFormation::Macro
    resource: CloudFormationResource
    name = 'DatetimeNow'
    description = 'Provides the current datetime as string in the format requested.'
    function_name = get_att(TransformFunction, "Arn")
