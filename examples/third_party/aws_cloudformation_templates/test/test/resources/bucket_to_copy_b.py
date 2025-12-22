"""BucketToCopyB - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyBTagFilter:
    resource: s3.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


@cloudformation_dataclass
class BucketToCopyB:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = [BucketToCopyBTagFilter]
