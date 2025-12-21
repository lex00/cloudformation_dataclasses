from __future__ import annotations

"""BucketToCopyB - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketToCopyBTagFilter:
    resource: TagFilter
    key = 'TestKey'
    value = 'my %s bucket %d'


@cloudformation_dataclass
class BucketToCopyB:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    tags = [BucketToCopyBTagFilter]
