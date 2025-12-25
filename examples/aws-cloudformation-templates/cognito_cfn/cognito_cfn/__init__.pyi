"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cognito
from .params import *  # noqa: F403, F401

from .params import AppName as AppName
from .params import CallbackURL as CallbackURL
from .security import Client as Client
from .security import Domain as Domain
from .security import UserPool as UserPool
from .security import UserPoolAdminCreateUserConfig as UserPoolAdminCreateUserConfig
from .security import UserPoolSchemaAttribute as UserPoolSchemaAttribute
from .security import UserPoolSchemaAttribute1 as UserPoolSchemaAttribute1
from .security import UserPoolSchemaAttribute2 as UserPoolSchemaAttribute2

__all__: list[str] = ['AppName', 'CallbackURL', 'Client', 'Domain', 'Parameter', 'STRING', 'Template', 'UserPool', 'UserPoolAdminCreateUserConfig', 'UserPoolSchemaAttribute', 'UserPoolSchemaAttribute1', 'UserPoolSchemaAttribute2', 'cloudformation_dataclass', 'cognito', 'get_att', 'ref', 'setup_resources']
