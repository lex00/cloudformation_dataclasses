"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation, lambda_
from .params import *  # noqa: F403, F401

from .infra import Macro as Macro
from .main import MacroFunction as MacroFunction
from .main import MacroFunctionEnvironment as MacroFunctionEnvironment
from .main import ResourceFunction as ResourceFunction

__all__: list[str] = ['CloudFormationResource', 'Macro', 'MacroFunction', 'MacroFunctionEnvironment', 'ResourceFunction', 'Template', 'cloudformation', 'cloudformation_dataclass', 'get_att', 'lambda_', 'ref', 'setup_resources']
