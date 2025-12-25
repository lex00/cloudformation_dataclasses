"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Mapping,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import s3
from .params import *  # noqa: F403, F401

from .params import BucketMapMapping as BucketMapMapping
from .storage import Bucket as Bucket
from .storage import BucketOwnershipControls as BucketOwnershipControls
from .storage import BucketOwnershipControlsRule as BucketOwnershipControlsRule
from .storage import NonExplodingBucket as NonExplodingBucket

__all__: list[str] = ['Bucket', 'BucketMapMapping', 'BucketOwnershipControls', 'BucketOwnershipControlsRule', 'Mapping', 'NonExplodingBucket', 'Template', 'cloudformation_dataclass', 'get_att', 'ref', 's3', 'setup_resources']
