"""EC2InstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class EC2InstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    path = '/'
    roles = [ref(EC2Role)]
