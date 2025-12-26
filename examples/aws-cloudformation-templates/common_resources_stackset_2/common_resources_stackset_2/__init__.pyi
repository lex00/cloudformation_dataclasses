"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import cloudformation

from .infra import StackSet as StackSet
from .infra import StackSetAutoDeployment as StackSetAutoDeployment
from .infra import StackSetDeploymentTargets as StackSetDeploymentTargets
from .infra import StackSetOperationPreferences as StackSetOperationPreferences
from .infra import StackSetParameter as StackSetParameter
from .infra import StackSetParameter1 as StackSetParameter1
from .infra import StackSetStackInstances as StackSetStackInstances
from .params import KmsKeyId as KmsKeyId
from .params import OUID as OUID
from .params import StackSetRegions as StackSetRegions

__all__: list[str] = ['KmsKeyId', 'OUID', 'Parameter', 'ParameterType', 'STRING', 'StackSet', 'StackSetAutoDeployment', 'StackSetDeploymentTargets', 'StackSetOperationPreferences', 'StackSetParameter', 'StackSetParameter1', 'StackSetRegions', 'StackSetStackInstances', 'Template', 'cloudformation', 'cloudformation_dataclass', 'get_att', 'ref', 'setup_resources']
