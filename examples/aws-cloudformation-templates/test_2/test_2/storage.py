"""Storage resources: Bucket, NonExplodingBucket."""

from . import *  # noqa: F403


@cloudformation_dataclass
class BucketOwnershipControlsRule:
    resource: s3.bucket.OwnershipControlsRule
    # Unknown CF key: ExpirationInDays = '!Explode Retention'
    # Unknown CF key: Status = 'Enabled'


@cloudformation_dataclass
class BucketOwnershipControls:
    resource: s3.bucket.OwnershipControls
    rules = [BucketOwnershipControlsRule]


@cloudformation_dataclass
class Bucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
    lifecycle_configuration = BucketOwnershipControls


@cloudformation_dataclass
class NonExplodingBucket:
    """AWS::S3::Bucket resource."""

    resource: s3.Bucket
