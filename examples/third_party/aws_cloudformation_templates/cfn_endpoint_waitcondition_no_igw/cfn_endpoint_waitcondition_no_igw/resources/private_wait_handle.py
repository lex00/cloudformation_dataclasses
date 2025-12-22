from __future__ import annotations

"""PrivateWaitHandle - AWS::CloudFormation::WaitConditionHandle resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateWaitHandle:
    """AWS::CloudFormation::WaitConditionHandle resource."""

    resource: WaitConditionHandle
