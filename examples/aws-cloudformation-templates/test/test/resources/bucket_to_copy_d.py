"""BucketToCopyD - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyDTagFilter:
    resource: s3.bucket.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


@cloudformation_dataclass
class BucketToCopyD:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = [BucketToCopyDTagFilter]
