"""Bucket1 - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class Bucket1:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
