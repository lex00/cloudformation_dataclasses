"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    STRING,
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
from .database import MyRDSParamGroup as MyRDSParamGroup
from .outputs import JDBCConnectionStringOutput as JDBCConnectionStringOutput
from .params import DBName as DBName
from .params import DBUser as DBUser

__all__: list[str] = ['DBName', 'DBUser', 'JDBCConnectionStringOutput', 'Join', 'MyDB', 'MyRDSParamGroup', 'Output', 'Parameter', 'STRING', 'Template', 'cloudformation_dataclass', 'get_att', 'rds', 'ref', 'setup_resources']
