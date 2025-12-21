from __future__ import annotations

"""PrivateWaitCondition - AWS::CloudFormation::WaitCondition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateWaitCondition:
    """AWS::CloudFormation::WaitCondition resource."""

    resource: WaitCondition
    handle: Ref[PrivateWaitHandle] = ref()
    timeout = '3600'
    count = 1
    depends_on = ["PrivateInstance"]
