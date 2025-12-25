"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import s3
from .params import *  # noqa: F403, F401

from .storage import Bucket1 as Bucket1

__all__: list[str] = ['Bucket1', 'Template', 'cloudformation_dataclass', 'get_att', 'ref', 's3', 'setup_resources']
