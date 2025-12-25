"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
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

from .params import Tags as Tags
from .storage import S3Bucket as S3Bucket

__all__: list[str] = ['Parameter', 'ParameterType', 'S3Bucket', 'Tags', 'Template', 'cloudformation_dataclass', 'get_att', 'ref', 's3', 'setup_resources']
