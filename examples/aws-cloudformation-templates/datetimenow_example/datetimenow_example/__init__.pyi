"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import s3
from cloudformation_dataclasses.intrinsics import Transform

from .storage import S3Bucket as S3Bucket
from .storage import S3BucketTagFilter as S3BucketTagFilter

__all__: list[str] = ['S3Bucket', 'S3BucketTagFilter', 'Template', 'Transform', 'cloudformation_dataclass', 'get_att', 'ref', 's3', 'setup_resources']
