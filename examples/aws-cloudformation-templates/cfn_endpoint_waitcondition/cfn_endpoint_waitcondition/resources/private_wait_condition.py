"""PrivateWaitCondition - AWS::CloudFormation::WaitCondition resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateWaitCondition:
    """AWS::CloudFormation::WaitCondition resource."""

    resource: WaitCondition
    handle = ref(PrivateWaitHandle)
    timeout = '3600'
    count = 1
    depends_on = ["PrivateInstance"]
