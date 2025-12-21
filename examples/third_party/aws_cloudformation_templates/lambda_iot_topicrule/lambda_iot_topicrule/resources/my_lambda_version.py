from __future__ import annotations

"""MyLambdaVersion - AWS::Lambda::Version resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class MyLambdaVersion:
    """AWS::Lambda::Version resource."""

    resource: Version
    function_name: Ref[MyLambda] = ref()
    depends_on = ["MyLambda"]
