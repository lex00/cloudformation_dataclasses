from __future__ import annotations

"""BucketToCopyA - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyATagFilter:
    resource: TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


@cloudformation_dataclass
class BucketToCopyA:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    tags = [BucketToCopyATagFilter]
