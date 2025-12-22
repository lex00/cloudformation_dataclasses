"""S3Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketTagFilter:
    resource: TagFilter
    key = 'Current'
    value = Transform(name='Date', parameters={
    'Date': ref(Date),
    'Operation': 'Current',
})


@cloudformation_dataclass
class S3BucketTagFilter1:
    resource: TagFilter
    key = 'Add'
    value = Transform(name='Date', parameters={
    'Date': ref(Date),
    'Days': ref(Days),
    'Operation': 'Add',
})


@cloudformation_dataclass
class S3BucketTagFilter2:
    resource: TagFilter
    key = 'Subtract'
    value = Transform(name='Date', parameters={
    'Date': ref(Date),
    'Days': ref(Days),
    'Operation': 'Subtract',
})


@cloudformation_dataclass
class S3BucketTagFilter3:
    resource: TagFilter
    key = 'Days'
    value = Transform(name='Date', parameters={
    'Date': ref(Date),
    'Date2': ref(Date2),
    'Operation': 'Days',
})


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    tags = [S3BucketTagFilter, S3BucketTagFilter1, S3BucketTagFilter2, S3BucketTagFilter3]
