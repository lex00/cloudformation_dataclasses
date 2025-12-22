from __future__ import annotations

"""GGSampleFunctionVersion - AWS::Lambda::Version resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class GGSampleFunctionVersion:
    """AWS::Lambda::Version resource."""

    resource: Version
    function_name = get_att(GGSampleFunction, "Arn")
