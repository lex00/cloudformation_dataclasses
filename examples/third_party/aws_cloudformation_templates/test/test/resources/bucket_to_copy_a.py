"""BucketToCopyA - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyATagFilter:
    resource: s3.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


@cloudformation_dataclass
class BucketToCopyA:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = [BucketToCopyATagFilter]
