from __future__ import annotations

"""BucketToCopyC - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyCTagFilter:
    resource: TagFilter
    key = 'TestKey'
    value = 'my bucket %d'


@cloudformation_dataclass
class BucketToCopyC:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    tags = [BucketToCopyCTagFilter]
