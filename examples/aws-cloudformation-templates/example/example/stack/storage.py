"""Storage resources: S3Bucket."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketTagFilter:
    resource: s3.bucket.TagFilter
    key = 'Upper'
    value = Transform(name='String', parameters={
    'InputString': ref(InputString),
    'Operation': 'Upper',
})


@cloudformation_dataclass
class S3BucketTagFilter1:
    resource: s3.bucket.TagFilter
    key = 'Lower'
    value = Transform(name='String', parameters={
    'InputString': ref(InputString),
    'Operation': 'Lower',
})


@cloudformation_dataclass
class S3BucketTagFilter2:
    resource: s3.bucket.TagFilter
    key = 'Capitalize'
    value = Transform(name='String', parameters={
    'InputString': ref(InputString),
    'Operation': 'Capitalize',
})


@cloudformation_dataclass
class S3BucketTagFilter3:
    resource: s3.bucket.TagFilter
    key = 'Title'
    value = Transform(name='String', parameters={
    'InputString': ref(InputString),
    'Operation': 'Title',
})


@cloudformation_dataclass
class S3BucketTagFilter4:
    resource: s3.bucket.TagFilter
    key = 'Replace'
    value = Transform(name='String', parameters={
    'InputString': ref(InputString),
    'Operation': 'Replace',
    'Old': ' ',
    'New': '_',
})


@cloudformation_dataclass
class S3BucketTagFilter5:
    resource: s3.bucket.TagFilter
    key = 'Strip'
    value = Transform(name='String', parameters={
    'InputString': ref(InputString),
    'Operation': 'Strip',
    'Chars': 'Tgif',
})


@cloudformation_dataclass
class S3BucketTagFilter6:
    resource: s3.bucket.TagFilter
    key = 'ShortenLeft'
    value = Transform(name='String', parameters={
    'InputString': ref(InputString),
    'Operation': 'MaxLength',
    'Length': 4,
    'StripFrom': 'Left',
})


@cloudformation_dataclass
class S3BucketTagFilter7:
    resource: s3.bucket.TagFilter
    key = 'ShortenRight'
    value = Transform(name='String', parameters={
    'InputString': ref(InputString),
    'Operation': 'MaxLength',
    'Length': 4,
})


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    tags = [S3BucketTagFilter, S3BucketTagFilter1, S3BucketTagFilter2, S3BucketTagFilter3, S3BucketTagFilter4, S3BucketTagFilter5, S3BucketTagFilter6, S3BucketTagFilter7]
