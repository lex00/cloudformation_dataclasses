"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
    Output,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation, cloudwatch
from .params import *  # noqa: F403, F401
from .outputs import *  # noqa: F403, F401

from .infra import Macro as Macro
from .main import MacroFunction as MacroFunction
from .main import ResourceFunction as ResourceFunction
from .monitoring import Dashboard as Dashboard
from .outputs import ResourceFunctionOutput as ResourceFunctionOutput

__all__: list[str] = ['CloudFormationResource', 'Dashboard', 'Macro', 'MacroFunction', 'Output', 'ResourceFunction', 'ResourceFunctionOutput', 'Template', 'cloudformation', 'cloudformation_dataclass', 'cloudwatch', 'get_att', 'ref', 'setup_resources']
