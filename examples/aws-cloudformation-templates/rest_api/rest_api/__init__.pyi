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
from cloudformation_dataclasses.aws import apigateway

from .main import Api as Api
from .main import ApiAuthorizer as ApiAuthorizer
from .main import ApiDeployment as ApiDeployment
from .main import ApiStage as ApiStage
from .params import AppName as AppName
from .params import UserPoolArn as UserPoolArn

__all__: list[str] = ['Api', 'ApiAuthorizer', 'ApiDeployment', 'ApiStage', 'AppName', 'Parameter', 'STRING', 'Template', 'UserPoolArn', 'apigateway', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources']
