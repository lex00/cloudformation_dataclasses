"""ADConnectorLinuxEC2DomainJoinInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorLinuxEC2DomainJoinInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    instance_profile_name = ref(ADConnectorLinuxEC2DomainJoinRole)
    path = '/'
    roles = [ref(ADConnectorLinuxEC2DomainJoinRole)]
    condition = 'LinuxEC2DomainJoinResourcesCondition'
