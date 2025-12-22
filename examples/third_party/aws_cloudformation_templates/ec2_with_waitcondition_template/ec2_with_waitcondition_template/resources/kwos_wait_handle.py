"""KWOSWaitHandle - AWS::CloudFormation::WaitConditionHandle resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KWOSWaitHandle:
    """AWS::CloudFormation::WaitConditionHandle resource."""

    resource: WaitConditionHandle
