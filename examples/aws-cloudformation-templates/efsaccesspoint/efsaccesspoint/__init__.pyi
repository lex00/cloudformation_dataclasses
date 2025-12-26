"""Auto-generated stub for IDE type checking."""

from cloudformation_dataclasses.core import (
    Output,
    Parameter,
    ParameterType,
    STRING,
    Template,
    cloudformation_dataclass,
    get_att,
    ref,
)
from cloudformation_dataclasses.core.resource_loader import setup_resources
from cloudformation_dataclasses.aws import efs

from .outputs import FileSystemIdOutput as FileSystemIdOutput
from .params import AccessPointName as AccessPointName
from .params import EFSFileSystemName as EFSFileSystemName
from .params import SecurityGroup1 as SecurityGroup1
from .params import SecurityGroup2 as SecurityGroup2
from .params import SecurityGroup3 as SecurityGroup3
from .params import Subnet1 as Subnet1
from .params import Subnet2 as Subnet2
from .params import Subnet3 as Subnet3
from .storage import EFSAccessPoint as EFSAccessPoint
from .storage import EFSAccessPointAccessPointTag as EFSAccessPointAccessPointTag
from .storage import EFSFileSystem as EFSFileSystem
from .storage import EFSFileSystemAccessPointTag as EFSFileSystemAccessPointTag
from .storage import EFSMountTarget1 as EFSMountTarget1
from .storage import EFSMountTarget2 as EFSMountTarget2
from .storage import EFSMountTarget3 as EFSMountTarget3

__all__: list[str] = ['AccessPointName', 'EFSAccessPoint', 'EFSAccessPointAccessPointTag', 'EFSFileSystem', 'EFSFileSystemAccessPointTag', 'EFSFileSystemName', 'EFSMountTarget1', 'EFSMountTarget2', 'EFSMountTarget3', 'FileSystemIdOutput', 'Output', 'Parameter', 'ParameterType', 'STRING', 'SecurityGroup1', 'SecurityGroup2', 'SecurityGroup3', 'Subnet1', 'Subnet2', 'Subnet3', 'Template', 'cloudformation_dataclass', 'efs', 'get_att', 'ref', 'setup_resources']
