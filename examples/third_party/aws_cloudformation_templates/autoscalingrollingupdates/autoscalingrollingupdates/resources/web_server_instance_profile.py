"""WebServerInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    resource: InstanceProfile
    path = '/'
    roles = [ref(DescribeHealthRole)]
