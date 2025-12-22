"""myInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class myInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    roles = ['DemoEC2SSMRole']
    instance_profile_name = 'myEC2SSMRole'
