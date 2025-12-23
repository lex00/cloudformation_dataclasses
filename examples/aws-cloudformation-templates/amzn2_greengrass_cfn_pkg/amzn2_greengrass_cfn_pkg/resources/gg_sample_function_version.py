"""GGSampleFunctionVersion - AWS::Lambda::Version resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GGSampleFunctionVersion:
    """AWS::Lambda::Version resource."""

    resource: lambda_.Version
    function_name = get_att(GGSampleFunction, "Arn")
