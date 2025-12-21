from __future__ import annotations

"""AWSManagedADWindowsEC2DomainJoinInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AWSManagedADWindowsEC2DomainJoinInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    instance_profile_name: Ref[AWSManagedADWindowsEC2DomainJoinRole] = ref()
    path = '/'
    roles = [ref("AWSManagedADWindowsEC2DomainJoinRole")]
    condition = 'WindowsEC2DomainJoinResourcesCondition'
