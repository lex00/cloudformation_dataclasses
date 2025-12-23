"""PropertyTypes for AWS::M2::Environment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from cloudformation_dataclasses.core.base import PropertyType, Tag
from cloudformation_dataclasses.intrinsics.functions import GetAtt, Ref, Sub


@dataclass
class EfsStorageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_point": "MountPoint",
        "file_system_id": "FileSystemId",
    }

    mount_point: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class FsxStorageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mount_point": "MountPoint",
        "file_system_id": "FileSystemId",
    }

    mount_point: Optional[Union[str, Ref, GetAtt, Sub]] = None
    file_system_id: Optional[Union[str, Ref, GetAtt, Sub]] = None


@dataclass
class HighAvailabilityConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "desired_capacity": "DesiredCapacity",
    }

    desired_capacity: Optional[Union[int, Ref, GetAtt, Sub]] = None


@dataclass
class StorageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "efs": "Efs",
        "fsx": "Fsx",
    }

    efs: Optional[EfsStorageConfiguration] = None
    fsx: Optional[FsxStorageConfiguration] = None

