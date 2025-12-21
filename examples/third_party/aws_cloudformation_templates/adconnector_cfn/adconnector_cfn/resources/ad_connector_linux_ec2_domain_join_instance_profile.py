from __future__ import annotations

"""ADConnectorLinuxEC2DomainJoinInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    instance_profile_name: Ref[ADConnectorLinuxEC2DomainJoinRole] = ref()
    path = '/'
    roles = [ref("ADConnectorLinuxEC2DomainJoinRole")]
    condition = 'LinuxEC2DomainJoinResourcesCondition'
