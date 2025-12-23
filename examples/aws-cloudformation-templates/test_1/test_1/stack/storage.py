"""Storage resources: BucketToCopyA, BucketToCopyB, BucketToCopyC, BucketToCopyD."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyATagFilter:
    resource: s3.bucket.TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


@cloudformation_dataclass
class BucketToCopyA:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = [BucketToCopyATagFilter]


@cloudformation_dataclass
class BucketToCopyBTagFilter:
    resource: s3.bucket.TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


@cloudformation_dataclass
class BucketToCopyB:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = [BucketToCopyBTagFilter]


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
