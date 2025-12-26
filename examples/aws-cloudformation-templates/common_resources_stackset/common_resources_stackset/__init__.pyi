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
from cloudformation_dataclasses.aws import cloudformation
from .params import *  # noqa: F403, F401

from .infra import StackSet as StackSet
from .infra import StackSetAutoDeployment as StackSetAutoDeployment
from .infra import StackSetDeploymentTargets as StackSetDeploymentTargets
from .infra import StackSetOperationPreferences as StackSetOperationPreferences
from .infra import StackSetParameter as StackSetParameter
from .infra import StackSetStackInstances as StackSetStackInstances
from .params import OUID as OUID

__all__: list[str] = ['OUID', 'Parameter', 'STRING', 'StackSet', 'StackSetAutoDeployment', 'StackSetDeploymentTargets', 'StackSetOperationPreferences', 'StackSetParameter', 'StackSetStackInstances', 'Template', 'cloudformation', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources']
