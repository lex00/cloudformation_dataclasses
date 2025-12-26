"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Parameter,
    ParameterType,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import Select

from .compute import Association1 as Association1
from .compute import Association2 as Association2
from .network import EIP1 as EIP1
from .network import EIP2 as EIP2
from .network import ENI as ENI
from .params import Subnet as Subnet

__all__: list[str] = ['Association1', 'Association2', 'EIP1', 'EIP2', 'ENI', 'Parameter', 'ParameterType', 'Select', 'Subnet', 'Template', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
