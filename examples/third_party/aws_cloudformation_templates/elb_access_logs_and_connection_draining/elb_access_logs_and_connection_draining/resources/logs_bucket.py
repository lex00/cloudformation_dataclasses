"""LogsBucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class LogsBucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    access_control = 'Private'
    deletion_policy = 'Retain'
