from __future__ import annotations

"""ADConnectorWindowsEC2DomainJoinInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    instance_profile_name: Ref[ADConnectorWindowsEC2DomainJoinRole] = ref()
    path = '/'
    roles = [ref("ADConnectorWindowsEC2DomainJoinRole")]
    condition = 'WindowsEC2DomainJoinResourcesCondition'
