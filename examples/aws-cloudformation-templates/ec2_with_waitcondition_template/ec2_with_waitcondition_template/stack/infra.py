"""Infra resources: KWOSWaitHandle, KWOSWaitCondition."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class KWOSWaitHandle:
    """AWS::CloudFormation::WaitConditionHandle resource."""

    resource: cloudformation.WaitConditionHandle


@cloudformation_dataclass
class KWOSWaitCondition:
    """AWS::CloudFormation::WaitCondition resource."""

    resource: cloudformation.WaitCondition
    handle = ref(KWOSWaitHandle)
    timeout = '300'
