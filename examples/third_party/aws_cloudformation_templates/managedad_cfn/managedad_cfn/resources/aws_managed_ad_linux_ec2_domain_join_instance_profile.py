from __future__ import annotations

"""AWSManagedADLinuxEC2DomainJoinInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class AWSManagedADLinuxEC2DomainJoinInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    instance_profile_name = ref(AWSManagedADLinuxEC2DomainJoinRole)
    path = '/'
    roles = [ref(AWSManagedADLinuxEC2DomainJoinRole)]
    condition = 'LinuxEC2DomainJoinResourcesCondition'
