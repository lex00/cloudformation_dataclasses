"""Infra resources: PrivateWaitHandle, PrivateWaitCondition."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class PrivateWaitHandle:
    """AWS::CloudFormation::WaitConditionHandle resource."""

    resource: cloudformation.WaitConditionHandle


@cloudformation_dataclass
class PrivateWaitCondition:
    """AWS::CloudFormation::WaitCondition resource."""

    resource: cloudformation.WaitCondition
    handle = ref(PrivateWaitHandle)
    timeout = '3600'
    count = 1
    depends_on = ["PrivateInstance"]
