from __future__ import annotations

"""S3Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class S3BucketTagFilter:
    resource: TagFilter
    key = 'Upper'
    value = Transform({
    'Name': 'String',
    'Parameters': {
        'InputString': ref(InputString),
        'Operation': 'Upper',
    },
})


@cloudformation_dataclass
class S3BucketTagFilter1:
    resource: TagFilter
    key = 'Lower'
    value = Transform({
    'Name': 'String',
    'Parameters': {
        'InputString': ref(InputString),
        'Operation': 'Lower',
    },
})


@cloudformation_dataclass
class S3BucketTagFilter2:
    resource: TagFilter
    key = 'Capitalize'
    value = Transform({
    'Name': 'String',
    'Parameters': {
        'InputString': ref(InputString),
        'Operation': 'Capitalize',
    },
})


@cloudformation_dataclass
class S3BucketTagFilter3:
    resource: TagFilter
    key = 'Title'
    value = Transform({
    'Name': 'String',
    'Parameters': {
        'InputString': ref(InputString),
        'Operation': 'Title',
    },
})


@cloudformation_dataclass
class S3BucketTagFilter4:
    resource: TagFilter
    key = 'Replace'
    value = Transform({
    'Name': 'String',
    'Parameters': {
        'InputString': ref(InputString),
        'Operation': 'Replace',
        'Old': ' ',
        'New': '_',
    },
})


@cloudformation_dataclass
class S3BucketTagFilter5:
    resource: TagFilter
    key = 'Strip'
    value = Transform({
    'Name': 'String',
    'Parameters': {
        'InputString': ref(InputString),
        'Operation': 'Strip',
        'Chars': 'Tgif',
    },
})


@cloudformation_dataclass
class S3BucketTagFilter6:
    resource: TagFilter
    key = 'ShortenLeft'
    value = Transform({
    'Name': 'String',
    'Parameters': {
        'InputString': ref(InputString),
        'Operation': 'MaxLength',
        'Length': 4,
        'StripFrom': 'Left',
    },
})


@cloudformation_dataclass
class S3BucketTagFilter7:
    resource: TagFilter
    key = 'ShortenRight'
    value = Transform({
    'Name': 'String',
    'Parameters': {
        'InputString': ref(InputString),
        'Operation': 'MaxLength',
        'Length': 4,
    },
})


@cloudformation_dataclass
class S3Bucket:
    """AWS::S3::Bucket resource."""

    resource: Bucket
    tags = [S3BucketTagFilter, S3BucketTagFilter1, S3BucketTagFilter2, S3BucketTagFilter3, S3BucketTagFilter4, S3BucketTagFilter5, S3BucketTagFilter6, S3BucketTagFilter7]
