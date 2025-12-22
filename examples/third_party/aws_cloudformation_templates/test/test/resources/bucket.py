from __future__ import annotations

"""Bucket - AWS::S3::Bucket resource."""

from .. import *  # noqa: F403


@cloudformation_dataclass
class BucketRule:
    resource: Rule
    expiration_in_days = '!Explode Retention'
    status = 'Enabled'


@cloudformation_dataclass
class BucketLifecycleConfiguration:
    resource: LifecycleConfiguration
    rules = [BucketRule]


@cloudformation_dataclass
class Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    lifecycle_configuration = BucketLifecycleConfiguration
