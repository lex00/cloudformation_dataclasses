"""LambdaEdgeVersion - AWS::Lambda::Version resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaEdgeVersion:
    """AWS::Lambda::Version resource."""

    resource: lambda_.Version
    function_name = ref(LambdaEdgeFunction)
