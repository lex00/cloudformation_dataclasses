"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import ec2
from cloudformation_dataclasses.intrinsics import Base64, Sub
from .params import *  # noqa: F403, F401

from .compute import Instance as Instance
from .compute import InstanceBlockDeviceMapping as InstanceBlockDeviceMapping
from .compute import InstanceEbs as InstanceEbs

__all__: list[str] = ['Base64', 'Instance', 'InstanceBlockDeviceMapping', 'InstanceEbs', 'Sub', 'Template', 'cloudformation_dataclass', 'ec2', 'get_att', 'ref', 'setup_resources']
