"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    NUMBER,
    Parameter,
    ParameterType,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import s3
from .params import *  # noqa: F403, F401

from .params import TestCount as TestCount
from .params import TestList as TestList
from .storage import BucketToCopyA as BucketToCopyA
from .storage import BucketToCopyATagFilter as BucketToCopyATagFilter
from .storage import BucketToCopyB as BucketToCopyB
from .storage import BucketToCopyBTagFilter as BucketToCopyBTagFilter
from .storage import BucketToCopyC as BucketToCopyC
from .storage import BucketToCopyCTagFilter as BucketToCopyCTagFilter
from .storage import BucketToCopyD as BucketToCopyD
from .storage import BucketToCopyDTagFilter as BucketToCopyDTagFilter

__all__: list[str] = ['BucketToCopyA', 'BucketToCopyATagFilter', 'BucketToCopyB', 'BucketToCopyBTagFilter', 'BucketToCopyC', 'BucketToCopyCTagFilter', 'BucketToCopyD', 'BucketToCopyDTagFilter', 'NUMBER', 'Parameter', 'ParameterType', 'Template', 'TestCount', 'TestList', 'cloudformation_dataclass', 'get_att', 'ref', 's3', 'setup_resources']
