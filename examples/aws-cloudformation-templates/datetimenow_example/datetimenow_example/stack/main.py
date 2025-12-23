"""Stack resources."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketTagFilter:
    resource: s3.bucket.TagFilter
    key = 'DatetimeNow'
    value = Transform(name='DatetimeNow', parameters={
    'format': '%Y-%m-%dT%H:%M:%SZ',
})


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = [S3BucketTagFilter]
