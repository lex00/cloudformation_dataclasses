"""WebServerInstanceProfile - AWS::IAM::InstanceProfile resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class WebServerInstanceProfile:
    """AWS::IAM::InstanceProfile resource."""

    # Unknown resource type: AWS::IAM::InstanceProfile
    resource: CloudFormationResource
    path = '/'
    roles = [ref(DescribeHealthRole)]
