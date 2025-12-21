from __future__ import annotations

"""KWOSWaitCondition - AWS::CloudFormation::WaitCondition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KWOSWaitCondition:
    """AWS::CloudFormation::WaitCondition resource."""

    resource: WaitCondition
    handle: Ref[KWOSWaitHandle] = ref()
    timeout = '300'
