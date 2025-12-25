"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import rds
from cloudformation_dataclasses.intrinsics import Join
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .database import MyDB as MyDB
from .outputs import JDBCConnectionStringOutput as JDBCConnectionStringOutput

__all__: list[str] = ['JDBCConnectionStringOutput', 'Join', 'MyDB', 'Output', 'Template', 'cloudformation_dataclass', 'get_att', 'rds', 'ref', 'setup_resources']
