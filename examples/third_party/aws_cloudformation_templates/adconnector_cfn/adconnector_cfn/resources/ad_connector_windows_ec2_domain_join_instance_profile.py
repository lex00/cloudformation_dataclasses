"""ADConnectorWindowsEC2DomainJoinInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class ADConnectorWindowsEC2DomainJoinInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: iam.InstanceProfile
    instance_profile_name = ref(ADConnectorWindowsEC2DomainJoinRole)
    path = '/'
    roles = [ref(ADConnectorWindowsEC2DomainJoinRole)]
    condition = 'WindowsEC2DomainJoinResourcesCondition'
