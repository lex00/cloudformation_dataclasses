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
from cloudformation_dataclasses.aws import rds, secretsmanager
from cloudformation_dataclasses.intrinsics import Sub

from .database import myDB as myDB
from .params import DBUser as DBUser
from .security import DBCredential as DBCredential
from .security import DBCredentialGenerateSecretString as DBCredentialGenerateSecretString

__all__: list[str] = ['DBCredential', 'DBCredentialGenerateSecretString', 'DBUser', 'Parameter', 'STRING', 'Sub', 'Template', 'cloudformation_dataclass', 'get_att', 'myDB', 'rds', 'ref', 'secretsmanager', 'setup_resources']
