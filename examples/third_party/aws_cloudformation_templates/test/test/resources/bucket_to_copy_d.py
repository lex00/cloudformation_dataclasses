from __future__ import annotations

"""BucketToCopyD - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyDTagFilter:
    resource: TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


@cloudformation_dataclass
class BucketToCopyD:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    tags = [BucketToCopyDTagFilter]
