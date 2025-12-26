"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    CloudFormationResource,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation

from .infra import Macro as Macro
from .main import Function as Function

__all__: list[str] = ['CloudFormationResource', 'Function', 'Macro', 'Template', 'cloudformation', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources']
