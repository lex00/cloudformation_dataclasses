"""BucketToCopyC - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyCTagFilter:
    resource: s3.bucket.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


@cloudformation_dataclass
class BucketToCopyC:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = [BucketToCopyCTagFilter]
