from __future__ import annotations

"""LambdaEdgeVersion - AWS::Lambda::Version resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LambdaEdgeVersion:
    """AWS::Lambda::Version resource."""

    resource: Version
    function_name: Ref[LambdaEdgeFunction] = ref()
