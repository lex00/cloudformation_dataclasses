from __future__ import annotations

"""S3Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketTagFilter:
    resource: TagFilter
    key = 'DatetimeNow'
    value = Transform(name='DatetimeNow', parameters={
    'format': '%Y-%m-%dT%H:%M:%SZ',
})


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    tags = [S3BucketTagFilter]
